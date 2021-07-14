from django.urls import path, include
from knox import views as knox_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('store', views.store, name="store"),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
]
