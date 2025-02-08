# Generated by Django 5.1.4 on 2025-01-15 09:33

from django.db import migrations
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_sku_remove_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
                ('product_image', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'productitems',
                'db_table': 'productitem',
            },
        ),
        migrations.AlterModelTable(
            name='productitem',
            table=None,
        ),
    ]
