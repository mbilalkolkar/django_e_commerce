from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, ProductItemViewSet, ProductViewSet, replenish_stock

router = routers.DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"product", ProductViewSet)
router.register(r"product-item", ProductItemViewSet)

app_name = "products"

urlpatterns = [
    path("", include(router.urls)),
    path('replenish-stock/<int:id>/<int:amount>/', replenish_stock, name="replenish_stock"),
]
