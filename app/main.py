import tornado.ioloop
import tornado.web
import cv2
import numpy as np
np.set_printoptions(precision=2)

import openface

'''
def get_rep(img_path):
    bgr_img = cv2.imread(img_path)
    import pdb; pdb.set_trace();
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    bb = align.getLargestFaceBoundingBox(rgb_img)
    aligned_face = align.align(args.img_d
'''

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
