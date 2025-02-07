from django.contrib import admin

from payments.models import Payment, PaymentType

# Register your models here.
admin.site.register([PaymentType, Payment])
