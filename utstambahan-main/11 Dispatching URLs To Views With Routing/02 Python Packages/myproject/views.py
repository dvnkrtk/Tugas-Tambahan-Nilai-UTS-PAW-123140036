from pyramid.response import Response

def home_view(request):
    return Response("Halo dunia! Ini aplikasi Pyramid dari package.")
