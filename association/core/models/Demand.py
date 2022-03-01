from django.db import models
from ._EntityTrait import EntityTrait

from core.models import Teasurer, Partner

STATUS_CHOICES = [
    ('CONCLUDED', 'Concluded'),
    ('PENDING', 'Pendente'),
    ('REFUSED', 'Recusado'),
]

class Demand(EntityTrait):
    
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES)
    teasurer = models.ForeignKey(Teasurer, blank=True, null=True, on_delete=models.SET_NULL)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'demand'
        
    def __str__(self):
        return self.message