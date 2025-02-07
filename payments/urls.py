from django.urls import include, path
from rest_framework import routers

from .views import PaymentViewSet

router = routers.DefaultRouter()
router.register(r"payments", PaymentViewSet)

app_name = "payments"

urlpatterns = [
    path("", include(router.urls)),
    path('generate-payment/', PaymentViewSet.as_view({'post': 'generate_payment'}), name='generate-payment'),

]
