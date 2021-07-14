from django.test import SimpleTestCase
from django.urls import reverse, resolve
from consumer.views import index, LoginAPI, RegisterAPI
from knox.views import LogoutView, LogoutAllView

# this is the Test case for the urls,
# so now we'll be checking for the index url
class TestUrls(SimpleTestCase):
    def setUp(self):
        self.url = reverse("index")
        self.login = reverse("login")
        self.logout = reverse("logout")
        self.logoutall = reverse("logoutall")
        self.register = reverse("register")

    def test_index_url_resolved(self):
        self.assertEquals(resolve(self.url).func, index)

    def test_login_url_resolved(self):
        self.assertEquals(resolve(self.login).func.view_class, LoginAPI)

    def test_logout_url_resolved(self):
        self.assertEquals(resolve(self.logout).func.view_class, LogoutView)

    def test_logout_all_url_resolved(self):
        self.assertEquals(resolve(self.logoutall).func.view_class, LogoutAllView)

    def test_register_url_resolved(self):
        self.assertEquals(resolve(self.register).func.view_class, RegisterAPI)