from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from core.models import Product

from django.shortcuts import render
from .models import Product, Category
# from core.models import Category

def gadgets_page(request):
    products = Product.objects.filter(category__name="Gadgets")
    return render(request, "Gadgets.html", {"products": products})

def nav_page(request):
    return render(request, "Gadgets.html")





def clothes_page(request):
    products = Product.objects.filter(category__name="Clothes")
    return render(request, "Clothes.html", {"products": products})

def nav1_page(request):
    return render(request, "Clothes.html")



def home_decor_page(request):
    products = Product.objects.filter(category__name="Home_decor")
    return render(request, "Home_decor.html", {"products": products})

def nav2_page(request):
    return render(request, "Home_decor.html")



def Books_page(request):
    products = Product.objects.filter(category__name="Books")
    return render(request, "Books.html", {"products": products})

def nav3_page(request):
    return render(request, "Books.html")



class HomeView(ListView):
    model = Product
    paginate_by = 6
    template_name = "base.html" 


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
    



def clothes_page(request):
    category = Category.objects.get(name="Clothes")
    products = Product.objects.filter(category=category)
    return render(request, "clothes.html", {"object_list": products})


def home_decor_page(request):
    category = Category.objects.get(name="Home decor")
    products = Product.objects.filter(category=category)
    return render(request, "home_decor.html", {"object_list": products})

def books_page(request):
    category = Category.objects.get(name="Books")
    products = Product.objects.filter(category=category)
    return render(request, "books.html", {"object_list": products})