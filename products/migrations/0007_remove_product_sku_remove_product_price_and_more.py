# Generated by Django 5.1.4 on 2025-01-15 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_category_options_category_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='SKU',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        # migrations.CreateModel(
        #     name='ProductItem',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('SKU', models.CharField(max_length=50)),
        #         ('stock', models.IntegerField()),
        #         ('price', models.FloatField()),
        #         ('product_image', models.CharField(max_length=50)),
        #         ('created', models.DateTimeField(auto_now_add=True)),
        #         ('modified', models.DateTimeField(auto_now=True)),
        #         ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
        #     ],
        #     options={
        #         'verbose_name': '',
        #         'verbose_name_plural': '',
        #         'db_table': 'ProductItem',
        #     },
        # ),
    ]
