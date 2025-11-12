# myproject/__init__.py
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('<h1>Home</h1>')

def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        config.add_route('home', '/')
        config.add_view(hello_world, route_name='home')
        return config.make_wsgi_app()
