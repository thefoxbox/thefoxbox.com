""" WSGI Gallery Controller """

from base import BaseController
from views.gallery import GalleryView

class GalleryController(BaseController):
    def view(self, environ, start_response):
        view = GalleryView()
        if hasattr(view, '__call__'):
            return view(environ)

