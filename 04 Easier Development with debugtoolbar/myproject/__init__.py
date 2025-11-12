from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('<h1>Hello Pyramid with Debug Toolbar!</h1>')

def main(global_config, **settings):
    """
    Application factory; dipanggil oleh pserve berdasarkan development.ini
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_debugtoolbar')

    config.add_route('home', '/')
    config.add_view(hello_world, route_name='home')

    return config.make_wsgi_app()