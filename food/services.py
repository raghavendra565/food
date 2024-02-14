from decimal import Decimal
from .models import Pricing


class PriceCalculatorService:
    @staticmethod
    def calculate_total_price(zone, organization_id, total_distance, item_type):
        base_price = Decimal(0)
        per_km_price = Decimal(0)
        
        
        try:
            pricing = Pricing.objects.get(organization_id=organization_id, zone=zone, item__type=item_type)
            base_price = pricing.fix_price
            per_km_price = pricing.km_price
        except Pricing.DoesNotExist:
            return None  
        
        
        if total_distance <= pricing.base_distance_in_km:
            total_price = base_price
        else:
            extra_distance = total_distance - pricing.base_distance_in_km
            total_price = base_price + (extra_distance * per_km_price)
        
        return total_price