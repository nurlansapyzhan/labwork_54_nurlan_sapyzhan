from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from labwork54.models import Product


def products_view(request: WSGIRequest):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})
