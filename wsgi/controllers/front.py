""" WSGI Front Controller """

from webob import Response
from views.front import FrontView

class FrontController(object):
    def __call__(self, action, environ, start_response):
        if not hasattr(self, action):
            return None

        action = getattr(self, action)(environ, start_response)
        response = Response(action)
        return response(environ, start_response)

    def index(self, *args):
        view = FrontView()
        if hasattr(view, '__call__'):
            return view()

