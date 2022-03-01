from django.db import models
from ._EntityTrait import EntityTrait
from core.models import Member, Vehicle

class Justification(EntityTrait):
    message = models.CharField(max_length=200)
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'justification'
        
    def __str__(self):
        return self.message