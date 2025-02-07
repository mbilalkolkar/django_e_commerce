

from rest_framework import serializers
from orders.serializers import OrderSerializer
from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ('id', 'user', 'order', 'payment_type', 'payment_method', 'transaction_id', 'billing_address',
                  'card_number', 'expiration_date', 'cvv')
