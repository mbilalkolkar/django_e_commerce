from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from orders.models import Order, OrderItem
from orders.serializers import OrderItemSerializer, OrderSerializer
from payments.serializers import PaymentSerializer
from shopping_cart.models import ShoppingCart
from payments.models import Payment

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='generate-order')
    def generate_order(self, request):
        user = request.user
        cart_items = ShoppingCart.objects.filter(user=user)
        if not cart_items.exists():
            return Response({"detail": "No items in the shopping cart."},
                            status=status.HTTP_404_NOT_FOUND)

        order = Order.objects.create(
            user=user,
            total=0,
            shipping_address=request.data.get('shipping_address'),
            shipping_method_id=request.data.get('shipping_method'),
            status=Order.StatusChoices.PENDING
        )

        total = 0
        # move cart items to order items
        for cart_item in cart_items:
            product_item = cart_item.product_item
            total += cart_item.product_item.price * cart_item.quantity
            OrderItem.objects.create(
                product_item=product_item,
                order=order,
                quantity=cart_item.quantity,
                price=cart_item.product_item.price,
                status=OrderItem.StatusChoices.PENDING
            )
            # update stock count of product items
            if cart_item.quantity > product_item.stock:
                return Response({"detail": "Not enough stock for product item: " + product_item.name},
                                status=status.HTTP_400_BAD_REQUEST)
            product_item.stock -= cart_item.quantity
            product_item.save()
            cart_item.delete()

        order.total = total
        order.save()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        # return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrderItem.objects.filter(order__user=self.request.user)
