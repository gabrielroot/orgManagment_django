from django.db import models
from ._EntityTrait import EntityTrait

class Cashier(EntityTrait):
    
    balance = models.FloatField()
    
    class Meta:
        ordering = ["balance"]
        db_table = 'cashier'