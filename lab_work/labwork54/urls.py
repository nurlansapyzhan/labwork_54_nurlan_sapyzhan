from django.urls import path

from labwork54.views.base import product_view

urlpatterns = [
    path('', product_view),
    path('products', product_view),
]
