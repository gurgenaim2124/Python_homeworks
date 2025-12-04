"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from core.views import  HomeView, ProductDetailView
from django.conf import settings
from django.views.generic import TemplateView
from core.views import nav_page, nav1_page, nav2_page, nav3_page
from core.views import gadgets_page, clothes_page, home_decor_page, books_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name= 'products'),
    path("product/<int:pk>/", ProductDetailView.as_view(), name= 'product-details'),
    # path("Gadgets.html/", nav_page, name='nav'), 
    # path("gadgets/", gadgets_page, name='gadgets'),

    # path("Clothes.html/", nav1_page, name='nav1'), 
    # path("clothes/", clothes_page, name='clothes'),

    # path("Home_decor.html/", nav2_page, name='nav2'), 
    # path("home_decor/", home_decor_page, name='home_decor'),
    
    # path("Books.html/", nav3_page, name='nav3'), 
    # path("books/", Books_page, name='books'),
    
    path("gadgets/", gadgets_page, name="gadgets"),
    path("clothes/", clothes_page, name="clothes"),
    path("home_decor/", home_decor_page, name="home_decor"),
    path("books/", books_page, name="books"),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)