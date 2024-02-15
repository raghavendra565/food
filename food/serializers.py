from rest_framework import serializers
from .models import Organization, Item, Pricing

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'

class CalculateDeliveryCostSerializer(serializers.Serializer):
    organization_id = serializers.CharField()
    total_distance = serializers.FloatField()
    item_id = serializers.CharField()
    zone = serializers.CharField()