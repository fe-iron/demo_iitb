from django.test import TestCase, Client
from django.urls import reverse, path, include
from consumer.models import Outfit
from rest_framework.test import APITestCase, URLPatternsTestCase
import json


class TestView(TestCase):
    """
        This is the test cases for the views and viewsets of the project
    """
    def setUp(self):
        self.client = Client()
        self.index_urls = reverse("index")
        self.store_outfit_url = reverse("store")
        self.register = reverse("register")
        self.login = reverse("login")
        self.outfit1 = Outfit.objects.create(
            category='girls outfit',
            name="Lengha",
            price=6999
        )

    def test_project_index_view(self):
        response = self.client.get(self.index_urls)

        self.assertEquals(response.status_code, 200)

    def test_register_index_view(self):
        data = {
            'username': "user1",
            "email": "email@email.com",
            "password": "123456"
        }
        response = self.client.post(self.register, data)

        self.assertEquals(response.status_code, 200)


    def test_store_data_view(self):
        data = {
            "category": "girls outfit",
            "name": "Lengha",
            "price": 6999
        }
        response = self.client.post(self.store_outfit_url, data)

        self.assertEquals(response.status_code, 200)


# Stuck at this class API
class OutfitTests(APITestCase, URLPatternsTestCase):
    """
        Ensure we can create a new account object.
    """
    urlpatterns = [
        path('api/', include('consumer.urls')),
    ]

    def test_create_account(self):
        # url = reverse('api/outfit/', urlconf=self.urlpatterns)
        # response = self.client.get(url, format='json')
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.data), 1)
        pass