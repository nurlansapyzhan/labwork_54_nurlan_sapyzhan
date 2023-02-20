from django.urls import path

from labwork54.views.base import products_view

from labwork54.views.products import product_view

urlpatterns = [
    path('', products_view, name='index'),
    path('products', products_view, name='index'),
    path('products/<int:pk>', product_view, name='product_detail')
]
