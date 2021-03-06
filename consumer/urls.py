from django.urls import path, include
from knox import views as knox_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('store', views.store, name="store"),
    path('api/tag/', views.filterTag, name='tag'),
    path('api/cloth', views.cloth, name='cloth'),
    path('api/mycloth/', views.MyCloth.as_view(), name='mycloth'),
    path('api/category/', views.filterCategory, name='category'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
