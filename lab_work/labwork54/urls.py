from django.urls import path

from labwork54.views.base import product_view

from labwork54.views.products import detail_view

urlpatterns = [
    path('', product_view, name='index'),
    path('products', product_view, name='index'),
    path('products/<int:pk>', detail_view, name='product_detail')
]
