from rest_framework import serializers
from orders.models import Order, OrderItem
from products.serializers import ProductItemSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product_item = ProductItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True,  source='order_items')  # source='orderitem_set')

    class Meta:
        model = Order
        fields = ('id', 'user', 'shipping_address', 'shipping_method', 'items')
