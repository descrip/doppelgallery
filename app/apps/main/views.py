import tornado.web
import StringIO
from PIL import Image
import os
from random import randint
from image_db import ImageDB
from get_rep import getRep
import psycopg2

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

def get_top_3(fname):
    idb = ImageDB()
    idb.load_from_file("test_save")

    mat = getRep(fname)
    if mat is None:
        raise Exception("couldn't find face")
    dists, names = idb.k_nearest(mat, 3)
    return dists, names

def handle_post(self, img_bytes):
    user_id = get_new_user_id()
    write_bytes_to_file(img_bytes, user_id)
    return '/gallery/%d' % user_id

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        self.redirect(handle_post(self, self.request.files['photo'][0]['body']))

class WebcamHandler(tornado.web.RequestHandler):
    def post(self):
        self.write(handle_post(self, self.request.files['webcam'][0]['body']))

class GalleryHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        conn = psycopg2.connect(database='dop', user='ubuntu', host='localhost', port='26257')
	cur = conn.cursor()

        img_file = get_img_by_user_id(user_id)
        try:
            x = get_top_3('/root/doppelganger/app/static/img/users/' + img_file)

            p = []
            for i in range(3):
                p.append((x[0][i], x[1][i]))
            p.sort()

            paintings = []
            cur.execute(
                "SELECT * FROM images WHERE id IN ('%s', '%s', '%s')" % \
                tuple([y[1] + ".jpg" for y in p])
            )
            er = list(cur)
            for pp in p:
                for r in er:
                    if r[0] == pp[1] + ".jpg":
                        d = {
                            'id' : pp[1],
                            'dist' : pp[0],
                            'artist' : r[1],
                            'title' : r[2],
                        }
                        paintings.append(d)
                        break
                else:
                    paintings.append({
                        'id' : pp[1],
                        'dist' : pp[0]
                    })

            with Image.open('./static/img/users/%s' % img_file) as user_img:
                self.render(
                    'gallery.html',
                    user_id = user_id,
                    user_img_file = img_file,
                    user_img_width = user_img.width,
                    user_img_height = user_img.height,
                    paintings = paintings
                )
        except:
            self.redirect('/?face_error=1')
