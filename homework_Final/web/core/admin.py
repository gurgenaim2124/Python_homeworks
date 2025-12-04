from django.contrib import admin
from core.models import Product, Category
from .models import *
from django.utils.html import format_html
# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'get_image')
#     search_fields = ('name', 'description')

#     def get_image(self, obj):
#         if obj.thumbnails:
#             return format_html('<img src="{}" width="100" height="75" />', obj.thumbnails.url)
#         return "No Image"
#     get_image.short_description = 'Thumbnail'  


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'thumbnail_preview') 

    def thumbnail_preview(self, obj):
        if obj.thumbnails:
            return format_html('<img src="{}" width="100" height="75" />', obj.thumbnails.url)
        return "No Image"
    thumbnail_preview.short_description = 'Thumbnail'
    

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
