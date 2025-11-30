from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from core.models import Product

from django.shortcuts import render
from .models import Product

def gadgets_page(request):
    products = Product.objects.filter(category__name="Gadgets")
    return render(request, "Gadgets.html", {"products": products})
# Create your views here.


def nav_page(request):
    return render(request, "Gadgets.html")
class HomeView(ListView):
    model = Product
    paginate_by = 12
    template_name = "base.html" 


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
    