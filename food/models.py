from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    TYPE_CHOICES = (
        ('perishable', 'Perishable'),
        ('non-perishable', 'Non-Perishable'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.CharField(max_length=255)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.PositiveIntegerField()
    km_price = models.DecimalField(max_digits=5, decimal_places=2)
    fix_price = models.DecimalField(max_digits=7, decimal_places=2)