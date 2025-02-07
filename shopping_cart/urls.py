from django.urls import include, path
from rest_framework import routers

from .views import ShoppingCartViewSet

router = routers.DefaultRouter()
router.register(r"shopping-cart", ShoppingCartViewSet)

app_name = "shopping_cart"

urlpatterns = [
    path("", include(router.urls)),
]
