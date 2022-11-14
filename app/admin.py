from django.contrib import admin
from .models import Gallery
from .models import Identify
# Register your models here.

@admin.register(Gallery)
class ImageGallery(admin.ModelAdmin):
    list_element = [
    'id',
    'photo',
    'fistName',
    'lastName',
    'date'
    ]

@admin.register(Identify)
class ImageIdentify(admin.ModelAdmin):
    list_element = [
    'id',
    'photo'
    ]

