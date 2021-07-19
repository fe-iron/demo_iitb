from . import models
from . import serializers
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# it is simply a viewset of class based views, which automatically determines urlconf for us
@method_decorator(login_required(login_url="/api/login/"), name='dispatch')
class ClothesViewset(viewsets.ModelViewSet):
    queryset = models.Clothes.objects.all()
    serializer_class = serializers.ClothesSerializer



class OutfitViewset(viewsets.ModelViewSet):
    queryset = models.Outfit.objects.all()
    serializer_class = serializers.OutfitSerializer
