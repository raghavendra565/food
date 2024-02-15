from rest_framework import viewsets
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import Organization, Item, Pricing
from .serializers import OrganizationSerializer, ItemSerializer, PricingSerializer
from rest_framework.response import Response
from .serializers import CalculateDeliveryCostSerializer
from rest_framework.decorators import api_view 
from django.urls import path
from django.shortcuts import render
from django.urls import include, re_path
from decimal import *

def home(request):
    return render(request, 'home.html')


class OrganizationViewSet(viewsets.ModelViewSet):
    """ orggnizationAPI"""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

class CalculateDeliveryCost(APIView):
    @swagger_auto_schema(request_body=CalculateDeliveryCostSerializer)
    @action(detail=False, methods=['post'], serializer_class=CalculateDeliveryCostSerializer)
    def post(self, request, *args, **kwargs):
        """API to calculate Food Delivery Price"""
        serializer = CalculateDeliveryCostSerializer(data=request.data)
        if serializer.is_valid():
            organization_id = serializer.validated_data['organization_id']
            total_distance = serializer.validated_data['total_distance']
            item_id = serializer.validated_data['item_id']
            zone = serializer.validated_data['zone']
        
            total_price = self.calculate_price(zone, organization_id, total_distance, item_id)
            return Response({'total_price': total_price}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    def calculate_price(self, zone, organization_id, total_distance, item_id):
        base_price = Decimal(0)
        per_km_price = Decimal(0)
        
        try:
            pricing = Pricing.objects.get(organization_id=organization_id, zone=zone, item_id=item_id)
            base_price = pricing.fix_price
            per_km_price = pricing.km_price
        except Pricing.DoesNotExist:
            return Response({"error": "Pricing not found for the given parameters"}, status=status.HTTP_404_NOT_FOUND)
                
        if total_distance <= pricing.base_distance_in_km:
            total_price = base_price
        else:
            extra_distance = Decimal(total_distance - pricing.base_distance_in_km)
            total_price = base_price + (extra_distance * per_km_price)
        
        return total_price
