from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, ItemViewSet, PricingViewSet, home

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'items', ItemViewSet)
router.register(r'pricing', PricingViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),
]
