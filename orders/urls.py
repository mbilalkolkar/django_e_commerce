from django.urls import include, path
from rest_framework import routers

from .views import OrderViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register(r"order", OrderViewSet)
router.register(r"order-item", OrderItemViewSet)

app_name = "orders"

urlpatterns = [
    path("", include(router.urls)),
    path('generate-order/', OrderViewSet.as_view({'post': 'generate_order'}), name='generate-order'),

]
