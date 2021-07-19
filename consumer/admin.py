from django.contrib import admin
from .models import Outfit, Clothes
# Register your models here.

class AdminClothes(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'timestamp', 'stock')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Clothes, AdminClothes)
admin.site.register(Outfit)