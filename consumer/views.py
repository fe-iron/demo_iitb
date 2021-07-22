# from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from knox.auth import User

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
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.

# Cache lifetime
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# homepage with cached paging for fast loading
# @cache_page(CACHE_TTL)
def index(request):
    user = User.objects.all()
    return render(request, "index.html",{'user': user})

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


@login_required(login_url="/api/login/")
def filterTag(request):
    '''
    This method is for tag/name wise search
    :param request: request
    :return: Querysets
    '''
    if request.method == 'GET':
        query = request.GET.get('query', None)
        queries = query.split(" ")
        query_set = []
        clothes = Clothes.objects.all()
        for i in clothes:
            for j in queries:
                if j in i.category:
                    try:
                        query_set.index(i)
                    except ValueError:
                        query_set.append(i)
        query_set = serializers.serialize('json', query_set)
        return HttpResponse(query_set, content_type="application/json")


@login_required(login_url="/api/login/")
def filterCategory(request):
    '''
    This method is for category wise search
    :param request: request
    :return: Querysets
    '''
    if request.method == 'GET':
        query = request.GET.get('query', None)
        queries = query.split(" ")
        query_set = []
        clothes = Clothes.objects.all()
        for i in clothes:
            for j in queries:
                if j in i.category:
                    try:
                        query_set.index(i)
                    except ValueError:
                        query_set.append(i)
                # print("url: ", i.image1.url)
        query_set = serializers.serialize('json', query_set)
        return HttpResponse(query_set, content_type="application/json")


def cloth(request):
    '''
    This method is for any particular Cloth object based on the primary key
    :param request: request
    :return: Cloth Object
    '''
    pk = request.GET.get('pk', None)
    if Clothes.objects.filter(id=pk).exists():
        cloth = Clothes.objects.filter(id=pk)
        cloth = serializers.serialize('json', cloth)
        return HttpResponse(cloth, status=200)
    return HttpResponse({"result": False}, status=404)
