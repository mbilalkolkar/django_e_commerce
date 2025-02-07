from django.contrib import admin

from orders.models import Order, OrderItem, ShippingMethod

# Register your models here.
admin.site.register([Order, OrderItem, ShippingMethod])  # Registering models in the admin panel
