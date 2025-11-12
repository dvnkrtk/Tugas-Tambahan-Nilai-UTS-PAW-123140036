from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    return {'message': 'Selamat datang di contoh Handling Requests & Responses!'}

@view_config(route_name='greet', renderer='templates/greet.jinja2')
def greet_view(request):
    name = request.matchdict.get('name', 'Anonim')
    return {'name': name}

@view_config(route_name='form', renderer='templates/home.jinja2', request_method='GET')
def form_view_get(request):
    return {'message': 'Masukkan nama Anda di form!'}

@view_config(route_name='form', request_method='POST')
def form_view_post(request):
    name = request.params.get('name', 'Anonim')
    return HTTPFound(location=f'/greet/{name}')
