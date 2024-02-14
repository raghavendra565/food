from rest_framework import viewsets
from .models import Organization, Item, Pricing
from .serializers import OrganizationSerializer, ItemSerializer, PricingSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer