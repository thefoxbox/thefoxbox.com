import os, sys
from routes import Mapper
from webob import exc, Request, Response

sys.path.append(os.path.dirname(__file__))

import controllers

map = Mapper()
map.connect('front', '/', controller='front', action='index')
map.connect('music', '/music/{section}/{page}.html', controller='music', action='view')
map.connect('article', '/article/{section}/{page}.html', controller='article', action='view')
map.connect('gallery', '/gallery/{page}.html', controller='gallery', action='view')

class TheFoxBox(object):
    def __call__(self, environ, start_response):
        controller = self.load_controller(environ, start_response)
        response = self.dispatch(controller, environ, start_response)

        if not response:
            return exc.HTTPNotFound()(environ, start_response)
        return response    

    def load_controller(self, environ, start_response):
        """Return controller instance from controller module."""
        req = Request(environ)
        match = map.match(req.path_info)
        if not match:
            return None
        controller = match['controller']
        return self.find_controller(controller)

    def find_controller(self, controller):
        """Import controller module."""
        module = 'controllers.' + controller
        __import__(module)
        class_name = controller.title() + 'Controller'
        if hasattr(sys.modules[module], class_name):
            return getattr(sys.modules[module], class_name)

    def dispatch(self, controller, environ, start_response):
        """Dispatch specified controller."""
        if not controller:
            return None
        controller = controller()
        req = Request(environ)
        match = map.match(req.path_info)
        if not match:
            return None
        action = match['action']
        return controller(action, environ, start_response)

application = TheFoxBox()

