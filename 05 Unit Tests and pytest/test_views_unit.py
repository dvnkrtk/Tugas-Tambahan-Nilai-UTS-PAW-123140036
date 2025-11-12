from pyramid.testing import DummyRequest
from myproject import views  # import module views

def test_home_view_returns_response():
    request = DummyRequest()
    request.registry = type("R", (), {"settings": {"myproject.site_name": "TestSite"}})()
    response = views.home_view(request)
    assert response.status_code == 200
    assert "TestSite" in response.text
