from django.urls import path

from labwork54.views.base import products_view, categories_view

from labwork54.views.products import product_view, category_add_view, product_add_view, category_delete_view, \
    category_update_view

urlpatterns = [
    path('', products_view, name='index'),
    path('products', products_view, name='index'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('categories/add', category_add_view, name='add_category'),
    path('products/add', product_add_view, name='add_product'),
    path('categories', categories_view, name='categories'),
    path('category/<int:pk>/delete', category_delete_view, name='delete_category'),
    path('category/<int:pk>/edit', category_update_view, name='edit_category')
]
