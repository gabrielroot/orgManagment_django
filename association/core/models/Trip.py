from django.db import models
from datetime import datetime
from ._EntityTrait import EntityTrait

from core.models import Vehicle

class Trip(EntityTrait):
    
    origin = models.CharField(max_length=200)
    destiny = models.CharField(max_length=200)
    startDate = models.DateTimeField(default=datetime.now)
    endDate = models.DateTimeField(null=True)
    kilometer = models.FloatField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'trip'
        
    def __str__(self):
        return self.destiny