from pyramid.view import view_config, view_defaults

@view_defaults(renderer='templates/class_template.jinja2')
class MyView:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'message': 'Halo Devina!', 'page': 'Home Page'}

    @view_config(route_name='about', renderer='templates/class_template.jinja2')
    def about(self):
        return {'message': 'Ini halaman About di Pyramid', 'page': 'About Page'}
