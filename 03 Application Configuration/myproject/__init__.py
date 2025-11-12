from pyramid.config import Configurator
from pyramid.response import Response

def hello_view(request):
    site_name = request.registry.settings.get("myproject.site_name", "My Project")
    return Response(f"Hello from {site_name}!")

def main(global_config, **settings):
    """
    Application factory: dipanggil oleh pserve. `settings` berisi nilai dari development.ini.
    """
    config = Configurator(settings=settings)
    config.include("pyramid_jinja2")

    config.add_route("home", "/")
    config.add_view(hello_view, route_name="home")

    return config.make_wsgi_app()
