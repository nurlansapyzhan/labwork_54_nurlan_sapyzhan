from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render, redirect

from labwork54.models import Product

from labwork54.models import Category


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    product.added_date = product.added_date.strftime("%d/%m/%Y %H:%M")
    return render(request, 'product_detail.html', context={'product': product})


def category_add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'category_add.html')
    category_data = {
        'category_name': request.POST.get('category_name'),
        'category_description': request.POST.get('category_description')
    }
    Category.objects.create(**category_data)
    return redirect('index')


def product_add_view(request: WSGIRequest):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'product_add.html', context={'categories': categories})
    product_data = {
        'product_name': request.POST.get('product_name'),
        'price': request.POST.get('price'),
        'image': request.POST.get('image'),
        'category_id': request.POST.get('category_id'),
        'description': request.POST.get('description')
    }
    product = Product.objects.create(**product_data)
    return redirect('product_detail', product.pk)


