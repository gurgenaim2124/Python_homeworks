from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from core.models import Product
# Create your views here.


class HomeView(ListView):
    model = Product
    paginate_by = 12
    template_name = "base.html"    


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
    