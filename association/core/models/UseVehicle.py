from django.db import models
from ._EntityTrait import EntityTrait

from core.models import Vehicle, Member

class UseVehicle(EntityTrait):
    
    justification = models.CharField(max_length=200)
    member = models.ForeignKey(Member, blank=True, null=True, on_delete=models.SET_NULL)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'use_vehicle'
        
    def __str__(self):
        return self.justification