import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")

    def post(self):
        photo_data = self.request.files['webcam'][0]['body']
        # do shit

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Test")
