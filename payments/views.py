from django.shortcuts import render
from rest_framework import viewsets, status
from orders.models import Order, OrderItem
from payments.models import Payment
from payments.serializers import PaymentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = []

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='generate-payment')
    def generate_payment(self, request):
        print(request.data)
        user = request.user
        order = Order.objects.filter(id=request.data.get('order')).first()
        # Process payment
        payment_method = request.data.get('payment_method')
        amount = order.total
        transaction_id = request.data.get("transaction_id")  # Replace with actual transaction ID from payment gateway

        payment = Payment.objects.create(
            user=user,
            order=order,
            amount=amount,
            payment_method=payment_method,
            # status='Completed',
            status=True,
            transaction_id=transaction_id,
            billing_address=request.data.get('billing_address'),

        )

        # update order status to confirmed
        order.status = Order.StatusChoices.CONFIRMED
        order.save()

        # order_items = order.orderitem_set.all()
        order_items = order.order_items.all()
        for order_item in order_items:
            # set status to confirmed in order_items
            order_item.status = OrderItem.StatusChoices.CONFIRMED
            order_item.save()

            # update stock count of product items in the order items
            # product_item = order_item.product_item
            # product_item.stock -= order_item.quantity
            # product_item.save()

        # return Response({'message': 'Payment generated successfully'}, status=status.HTTP_201_CREATED)

        return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
