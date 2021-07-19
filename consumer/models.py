from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# This model is for the clothes itself
class Clothes(models.Model):
    name        = models.CharField(max_length=200, unique=True)
    price       = models.IntegerField()
    tag         = models.CharField(max_length=100)
    category    = models.CharField(max_length=100)
    timestamp   = models.DateTimeField(auto_now=True)
    desc        = models.TextField()
    stock       = models.IntegerField(default=1)
    image1      = models.ImageField(upload_to="photos/clothes/", default=None)
    image2      = models.ImageField(upload_to="photos/clothes/", default=None)
    image3      = models.ImageField(upload_to="photos/clothes/", default=None)
    image4      = models.ImageField(upload_to="photos/clothes/", default=None)
    image5      = models.ImageField(upload_to="photos/clothes/", default=None)
    slug        = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Clothe'
        verbose_name_plural = 'Clothes'

    def get_url(self):
        return reverse('detailed-view', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Clothes, self).save(*args, **kwargs)


# Outfit model for Wardo app(consumer app), it only have category, name, price(If I'm missing something, let me know)
class Outfit(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, null=False, default="NaN")
    name = models.CharField(max_length=255, null=False, default="NaN")
    price = models.IntegerField(null=True, default="NaN")

    def __str__(self):
        return self.name
