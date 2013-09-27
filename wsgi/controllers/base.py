""" WSGI Base Controller """

from webob import Response

class BaseController(object):
    def __call__(self, action, environ, start_response):
        if not hasattr(self, action):
            return None

        action = getattr(self, action)(environ, start_response)
        response = Response(action)
        return response(environ, start_response)

