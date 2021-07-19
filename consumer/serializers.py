from .models import Outfit, Clothes
from rest_framework import serializers
from django.contrib.auth.models import User


#  Serializer class for Outfit model, it converts complex data types to native python data type like queryset,
#  models to native data types
class OutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outfit
        fields = '__all__'


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['name', 'price', 'tag', 'category', 'desc', 'stock', 'image1', 'image2', 'image3', 'image4', 'image5', "slug"]
        read_only_fields = ['slug']




# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user