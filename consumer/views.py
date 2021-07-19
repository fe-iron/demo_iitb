from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Outfit, Clothes
from django.conf import settings
from knox.models import AuthToken
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.views import LoginView as KnoxLoginView
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .serializers import UserSerializer, RegisterSerializer, ClothesSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer


# Create your views here.

# Cache lifetime
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# homepage with cached paging for fast loading
@cache_page(CACHE_TTL)
def index(request):
    return render(request, "index.html")

def store(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        price = request.POST.get('price', None)
        category = request.POST.get('category', None)

        outfit = Outfit(name=name, price=price, category=category)
        outfit.save()
        messages.info(request, "successfully created!")
        return render(request, "index.html")
    return render(request, "index.html")


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # login(request, user) line in below code, will also create session based authentication with
        # token based authentication.
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



# Clothes Tag API
@csrf_exempt
def filter(request):
    if request.method == 'POST':
        query = request.POST.get('query', None)
        query_set = []
        clothes = Clothes.objects.all()
        for i in clothes:
            if query in i.tag:
                query_set.append(i)
        query_set = serializers.serialize('json', query_set)
        return HttpResponse(query_set, content_type="application/json")