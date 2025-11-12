from pyramid.config import Configurator

def main(global_config, **settings):
    """Fungsi utama untuk membuat aplikasi Pyramid"""
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')  # contoh jika nanti pakai templating
        config.add_route('home', '/')
        config.add_view('myproject.views.home_view', route_name='home')
        app = config.make_wsgi_app()
    return app
