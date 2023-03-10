# Generated by Django 4.1.7 on 2023-02-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labwork54', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=200000, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
