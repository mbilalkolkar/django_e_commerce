from shopping_cart.models import ShoppingCart
from rest_framework import serializers


class ShoppingCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = '__all__'
