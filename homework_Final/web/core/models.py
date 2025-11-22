from django.db import models

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

    def __str__(self):
        return f"{self.name}"