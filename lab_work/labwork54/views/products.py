from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render

from labwork54.models import Product


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    product.added_date = product.added_date.strftime("%d/%m/%Y %H:%M")
    return render(request, 'product_detail.html', context={'product': product})
