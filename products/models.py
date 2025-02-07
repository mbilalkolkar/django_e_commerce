import re
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="children")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        # db_table = ''
        # managed = True #  table’s creation, modification, and deletion, ig true by default
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}, {self.parent.name if self.parent else 'No Parent'}"


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(max_length=100)
    # tags = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True, null=True)
    # price = models.FloatField()
    # stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    product_image_link = models.CharField(max_length=255, null=True)
    # image = models.ImageField(upload_to='products/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        """Unicode representation of Product."""
        return f"{self.name}, {self.category}"


class ProductItem(models.Model):
    # VALUES(%(product_id)s, %(SKU)s, %(quantity_in_stock)s, %(product_image)s, %(price)s, %(created_date)s, %(last_modified_date)s )"
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, related_name='items')
    SKU = models.CharField(max_length=50)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_image_link = models.CharField(max_length=255, null=True)
    # product_image = models.ImageField(upload_to='product_item/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        # db_table = "ProductItem"
        verbose_name = "ProductItem"
        verbose_name_plural = "ProductItems"

    @property
    def in_stock(self):
        return self.stock > 0

    def increase_stock(self, amount):
        self.stock += amount
        # self.save()
        return self.stock

    def __str__(self):
        return f"{self.product.name}, {self.SKU}, {self.stock}, {self.price}"


class ProductVariation(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "ProductVariation"


class ProductVariationOption(models.Model):
    variation = models.ForeignKey(ProductVariation, models.DO_NOTHING, null=True)
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name = "ProductVariationOption"


class ProductConfig(models.Model):
    product_item = models.ForeignKey(ProductItem, models.DO_NOTHING, null=True)
    variation_option = models.ForeignKey(ProductVariationOption, models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = "ProductConfig"
