""" WSGI Front View """

import os
import pystache

templates = os.path.join(os.path.dirname(__file__), 'templates')

class FrontView(object):
    def __call__(self):
        renderer = pystache.Renderer(search_dirs=templates)
        return renderer.render_name('front')

