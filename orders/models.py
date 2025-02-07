from django.db import models

from django.contrib.auth.models import AbstractUser, User

# from django.conf import settings
import uuid
from products.models import ProductItem
# class User(AbstractUser):
#     pass

# Create your models here.
from shopping_cart.models import ShoppingCart


class ShippingMethod(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.price}"


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "Pending"
        CONFIRMED = "Confirmed"
        CANCELLED = "Cancelled"

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_orders")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_orders")
    total = models.IntegerField()
    shipping_address = models.CharField(max_length=255)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # db_table = 'Order'
        verbose_name = "order"
        verbose_name_plural = "orders"

    def set_status(self, status):
        if status not in [self.StatusChoices.PENDING, self.StatusChoices.CONFIRMED, self.StatusChoices.CANCELLED]:
            return False
        self.status = status
        self.save()
        return True

    def __str__(self):
        return f"Order {self.id} by {self.user.username}, {self.status} "

    # def generate_order(self):
    #     """
    #     move data from shopping cart to order item
    #     calculate total
    #     save order
    #     """
    #     cart_items = ShoppingCart.objects.filter(user=self.user)
    #     total = 0
    #     for item in cart_items:
    #         total += item.product_item.price * item.quantity
    #         OrderItem.objects.create(
    #             product_item=item.product_item,
    #             order=self,
    #             quantity=item.quantity,
    #             price=item.product_item.price,
    #             status=OrderItem.StatusChoices.PENDING
    #         )
    #         item.delete()
    #     self.total = total
    #     self.save()
    #     return True


class OrderItem(models.Model):
    """Model definition for OrderItem."""
    class StatusChoices(models.TextChoices):
        PENDING = "Pending"
        CONFIRMED = "Confirmed"
        CANCELLED = "Cancelled"

    product_item = models.ForeignKey(ProductItem, on_delete=models.DO_NOTHING, null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, related_name="order_items")
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"

    @property
    def item_subtotal(self):
        return self.product_item.price * self.quantity

    def set_status(self, status):
        if status not in [self.StatusChoices.PENDING, self.StatusChoices.CONFIRMED, self.StatusChoices.CANCELLED]:
            return False
        self.status = status
        self.save()
        return True

    def __str__(self):
        """Unicode representation of OrderItem."""
        return f"{self.product_item.SKU} x {self.quantity} - {self.product_item.product.name} in Order {self.order.id}"
