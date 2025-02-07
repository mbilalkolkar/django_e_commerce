"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers
from oauth2_provider import urls as oauth2_urls
from api import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    # auth
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('o/', include(oauth2_urls)),
    # debug url
    path('__debug__/', include('debug_toolbar.urls')),
    # swagger API UI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # rest framework API
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # apps
    path("", include("products.urls", namespace="products")),
    path("", include("orders.urls", namespace="orders")),
    path("", include("shopping_cart.urls", namespace="shopping_cart")),
    path("", include("payments.urls", namespace="payments")),
]

# urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
