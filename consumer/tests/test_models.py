from django.test import TestCase
from consumer.models import Outfit

class TestBookModel(TestCase):
    """
       It ensures the correct creation of Outfit objects
    """
    def setUp(self):
        self.lengha = Outfit.objects.create(
            category='girls outfit',
            name="Lengha",
            price=6999
        )

    def test_book_model(self):
        self.assertEquals(self.lengha.category, "girls outfit")