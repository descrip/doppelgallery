import argparse
import tornado.ioloop
import tornado.web
import cv2
import numpy as np
np.set_printoptions(precision=2)

import argparse
import itertools
import os
import time

import openface

from lshash import LSHash

start = time.time()

fileDir = os.path.dirname(os.path.realpath(__file__))
modelDir = '/root/openface/models/'
dlibModelDir = os.path.join(modelDir, 'dlib')
openfaceModelDir = os.path.join(modelDir, 'openface')

parser = argparse.ArgumentParser()

parser.add_argument('imgs', type=str, nargs='+', help="Input images.")
parser.add_argument('--dlibFacePredictor', type=str, help="Path to dlib's face predictor.",
                    default=os.path.join(dlibModelDir, "shape_predictor_68_face_landmarks.dat"))
parser.add_argument('--networkModel', type=str, help="Path to Torch network model.",
                    default=os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'))
parser.add_argument('--imgDim', type=int,
                    help="Default image dimension.", default=96)
parser.add_argument('--verbose', action='store_true')

args = parser.parse_args()

align = openface.AlignDlib(args.dlibFacePredictor)
net = openface.TorchNeuralNet(args.networkModel, args.imgDim)
lsh = LSHash(32, 128)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def get_rep(imgPath):
    bgrImg = cv2.imread(imgPath)

    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    start = time.time()
    bb = align.getLargestFaceBoundingBox(rgbImg)
    if bb is None:
        raise Exception("Unable to find a face: {}".format(imgPath))

    start = time.time()
    alignedFace = align.align(args.imgDim, rgbImg, bb,
            landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    if alignedFace is None:
        raise Exception("Unable to align image: {}".format(imgPath))

    start = time.time()
    rep = net.forward(alignedFace)
    print rep

    return rep

def load_tests():
    for img in args.imgs:
        lsh.index(get_rep(img), img)

if __name__ == "__main__":
    '''
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
    '''
    load_tests()
    l = [get_rep(x) for x in args.imgs]
    import pdb; pdb.set_trace();
