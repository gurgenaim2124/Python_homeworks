from django.db import models
from django.utils.html import format_html

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2, default= 0.00)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnails = models.ImageField(upload_to="product_thumbnail/", null=True, blank=True)

    def get_image(self):
        return format_html('<img src="{}" width= "100" height= "75">'.format(self.thumbnails.url))


    def __str__(self):
        return f"{self.name}"
    
class Gadgets(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2, default= 0.00)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnails = models.ImageField(upload_to="product_thumbnail/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    


# class Item(models.Model):
#     name = models.CharField(max_length=100, null=False, default="name")
#     def __str__(self):
#         return self.name