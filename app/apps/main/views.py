import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        photo_data = self.request.files['photo'][0]['body']
        # do shit
        self.write('/gallery')

class WebcamHandler(tornado.web.RequestHandler):
    def post(self):
        photo_data = self.request.files['webcam'][0]['body']
        # do shit
        self.write('/gallery')

class GalleryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('gallery.html')
