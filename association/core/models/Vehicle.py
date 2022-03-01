from django.db import models
from ._EntityTrait import EntityTrait

class Vehicle(EntityTrait):
    
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    costPerKilometer = models.FloatField()
    costPerKilometer = models.FloatField()
    
    class Meta:
        ordering = ["model", "color", "costPerKilometer", "costPerKilometer"]
        db_table = 'vehicle'
        
    def __str__(self):
        return self.model