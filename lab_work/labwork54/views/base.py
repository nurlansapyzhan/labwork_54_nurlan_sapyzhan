from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from labwork54.models import Product

from labwork54.models import Category


def products_view(request: WSGIRequest):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})


def categories_view(request: WSGIRequest):
    categories = Category.objects.all()
    return render(request, 'categories.html', context={'categories': categories})
