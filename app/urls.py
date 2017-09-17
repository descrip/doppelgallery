from tornado import web
from tornado.web import URLSpec as url
from settings import settings
from utils import include

from apps.main.views import *

urls = [
    url(r"/", HomeHandler),
    url(r"/webcam", WebcamHandler),
    url(r"/upload", UploadHandler),
    url(r"/gallery", GalleryHandler),
    url(r"/static/(.*)", web.StaticFileHandler, {"path": settings.get('static_path')}),
]
# urls += include(r"/", "apps.main.urls")
