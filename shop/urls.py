"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

from shop import views



urlpatterns = [
    path('', views.ProductsListView.as_view(), name='product_list'),
    #path('cart_view/', TemplateView.as_view(template_name='shop/cart.html'), name='cart'),
    #path('detail/<int:pk>/', TemplateView.as_view(template_name='shop/single-product.html'), name='single_product')
]