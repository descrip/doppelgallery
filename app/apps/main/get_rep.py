import openface
import cv2
import os

# some initial variable setup (!)
# TODO figure out what this is doing
modelDir = '/root/openface/models/'
dlibModelDir = os.path.join(modelDir, 'dlib')
align = openface.AlignDlib(os.path.join(dlibModelDir, "shape_predictor_68_face_landmarks.dat"))
imgDim = 96
openfaceModelDir = os.path.join(modelDir, 'openface')
net = openface.TorchNeuralNet(os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'), imgDim)

def getRep(imgPath):

    # load some image
    bgrImg = cv2.imread(imgPath)

    # couldn't load image
    if bgrImg is None:
        return None

    # load some other image (rgb?)
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    # build the bounding box
    bb = align.getLargestFaceBoundingBox(rgbImg)

    # couldn't find a face, so we return none
    if bb is None:
        return None

    # build an aligned face
    alignedFace = align.align(imgDim, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

    # could not align face properly
    if alignedFace is None:
        return None
        # raise Exception("Unable to align image: {}".format(imgPath))

    # build the actual representation
    rep = net.forward(alignedFace)
    return rep
