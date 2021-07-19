from django.test import TestCase
from consumer.models import Outfit, Clothes

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
        self.kid = Clothes.objects.create(
            name = 'shirt',
            price = 399,
            tag = 'kid kid-shirt',
            category = 'kid wear',
            stock = 10,
            desc = "This is a kid clothe"
        )

    def test_outfit_model(self):
        self.assertEquals(self.lengha.category, "girls outfit")

    def test_clothe_model(self):
        self.assertEquals(self.kid.slug, "shirt")