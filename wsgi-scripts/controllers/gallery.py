""" WSGI Gallery Controller """

from webob import Response
from views.gallery import GalleryView

class GalleryController(object):
    def __call__(self, action, environ, start_response):
        if not hasattr(self, action):
            return None

        action = getattr(self, action)(environ, start_response)
        response = Response(action)
        return response(environ, start_response)

    def view(self, environ, start_response):
        view = GalleryView()
        if hasattr(view, '__call__'):
            return view(environ)

