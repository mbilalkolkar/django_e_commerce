from products.models import Product, Category, ProductItem
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return price


class ProductSerializer(serializers.ModelSerializer):
    items = ProductItemSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
