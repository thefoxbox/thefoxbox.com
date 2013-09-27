""" WSGI Error Controller """

from webob import Response
from views.error import ErrorView

class ErrorController(object):
    def __call__(self, action, environ, start_response):
        if not hasattr(self, action):
            return None

        action = getattr(self, action)(environ, start_response)
        response = Response(action)
        return response(environ, start_response)

    def not_found(self, *args):
        view = ErrorView()
        if hasattr(view, '__call__'):
            return view()

