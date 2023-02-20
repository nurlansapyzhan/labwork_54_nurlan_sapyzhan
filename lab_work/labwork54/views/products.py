from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render

from labwork54.models import Product


def detail_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', context={'product': product})