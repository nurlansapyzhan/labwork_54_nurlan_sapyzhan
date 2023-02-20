from django.db import models
from django.utils.datetime_safe import datetime


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=500, null=False, blank=False, verbose_name='Наименование категории')
    category_description = models.CharField(max_length=2000, null=True, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'Category - {self.category_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=500, null=False, blank=False, verbose_name='Наименование продукта')
    description = models.CharField(max_length=2000, null=True, verbose_name='Описание продукта')
    category = models.ForeignKey(to=Category, verbose_name='Категория продукта', null=False, blank=False,
                                 related_name='products', on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now=True, verbose_name='Дата и время добавления', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.CharField(max_length=200000, null=False, verbose_name='Изображение', default='')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Product - {self.product_name}'
