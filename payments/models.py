from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class PaymentType(models.Model):
    value = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.value}"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_payment')
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE, related_name='order_payment', null=True)
    payment_type = models.ForeignKey(PaymentType, models.DO_NOTHING, null=True)
    payment_method = models.CharField(max_length=255, null=True)
    billing_address = models.TextField(null=False)
    transaction_id = models.CharField(max_length=255, null=True)
    amount = models.FloatField(null=False)

    card_number = models.CharField(max_length=255, null=True)
    # card_holder_name = models.CharField(max_length=255, null=False)
    expiration_date = models.DateField(null=True)
    cvv = models.CharField(max_length=10, null=True)

    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.created}, {self.status}"
