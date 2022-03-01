from django.db import models
from datetime import datetime
from ._EntityTrait import EntityTrait
from core.models import Partner

class MontlyPayment(EntityTrait):
    
    paymenDate = models.DateTimeField(default=datetime.now)
    dueDate = models.DateTimeField(null=True)
    value = models.FloatField()
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'montly_payment'
        
    def __str__(self):
        return self.paymenDate