from django.db import models

from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product_item = models.ForeignKey("products.ProductItem", on_delete=models.DO_NOTHING, null=False)
    quantity = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product_item.SKU} - {self.product_item.product.name} - {self.quantity}"
