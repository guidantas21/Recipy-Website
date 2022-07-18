from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import home, create_post, sign_up, login


def test_url(self, url_name, view):
        url = reverse(url_name)
        print(resolve(url))
        self.assertEquals(resolve(url).func, view)


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        test_url(self, url_name='home', view=home)

    def test_create_post_url_is_resolved(self):
        test_url(self, url_name='create-post', view=create_post)

    def test_sign_up_url_is_resolved(self):
        test_url(self, url_name='sign-up', view=sign_up)

    def test_login_url_is_resolved(self):
        test_url(self, url_name='login', view=login)