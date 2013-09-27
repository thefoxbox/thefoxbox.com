from routes import Mapper

urls = Mapper()

urls.connect('front', '/', controller='front', action='index')
urls.connect('music', '/music/{section}/{page}.html', controller='music', action='view')
urls.connect('article', '/article/{section}/{page}.html', controller='article', action='view')
urls.connect('gallery', '/gallery/{page}.html', controller='gallery', action='view')
