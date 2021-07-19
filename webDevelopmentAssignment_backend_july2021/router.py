from consumer.viewsets import OutfitViewset, ClothesViewset
from rest_framework import routers


# it generates routes and return a hyperlinks to all the list views
router = routers.DefaultRouter()
router.register('clothes', ClothesViewset)