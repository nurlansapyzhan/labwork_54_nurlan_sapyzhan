# Generated by Django 4.1.7 on 2023-02-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labwork54', '0004_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Цена'),
        ),
    ]
