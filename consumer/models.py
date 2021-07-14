from django.db import models


# Outfit model for Wardo app(consumer app), it only have category, name, price(If I'm missing something, let me know)
class Outfit(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, null=False, default="NaN")
    name = models.CharField(max_length=255, null=False, default="NaN")
    price = models.IntegerField(null=True, default="NaN")

    def __str__(self):
        return self.name
