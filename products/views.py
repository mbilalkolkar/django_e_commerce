from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from products.serializers import CategorySerializer, ProductItemSerializer, ProductSerializer
from products.models import Category, Product, ProductItem
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


@api_view(["POST"])
@permission_classes([AllowAny])
def replenish_stock(request, id, amount):
    try:
        product_item = ProductItem.objects.get(pk=id)
        product_item.increase_stock(amount)
        product_item.save()
        return Response({"success": f"Stock increased to {product_item.stock}"})
    except ObjectDoesNotExist:
        return Response({"error": "Product item not found."}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductItemViewSet(viewsets.ModelViewSet):

    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def replenish_stock(request, id, amount):
    try:
        product_item = ProductItem.objects.get(pk=id)
        product_item.increase_stock(amount)
        product_item.save()
        return Response({"success": f"Stock increased to {product_item.stock}"})
    except ObjectDoesNotExist:
        return Response({"error": "Product item not found."}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
