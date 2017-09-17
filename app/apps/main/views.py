import tornado.web
import StringIO
from PIL import Image
import os
from random import randint
from image_db import ImageDB

def get_new_user_id():
    while True:
        x = randint(1, 999999999)
        if not get_img_by_user_id(x):
            return x

def write_bytes_to_file(img_bytes, user_id):
    img = Image.open(StringIO.StringIO(img_bytes))
    img.save("./static/img/users/%d.%s" % (user_id, img.format), img.format)

def get_img_by_user_id(user_id):
    for root, dirs, files in os.walk('./static/img/users'):
        for name in files:
            if str(user_id) in os.path.splitext(name)[0]:
                return name

def find_top_3(img_file):
    idb = ImageDB()

def handle_post(self, img_bytes):
    user_id = get_new_user_id()
    write_bytes_to_file(img_bytes, user_id)
    self.write('/gallery/%d' % user_id)

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        handle_post(self, self.request.files['photo'][0]['body'])

class WebcamHandler(tornado.web.RequestHandler):
    def post(self):
        handle_post(self, self.request.files['webcam'][0]['body'])

class GalleryHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        img_file = get_img_by_user_id(user_id)
        with Image.open('./static/img/users/%s' % img_file) as user_img:
            self.render(
                'gallery.html',
                user_id = user_id,
                user_img_file = img_file,
                user_img_width = user_img.width,
                user_img_height = user_img.height,
            )
