from django.db import models
from ._EntityTrait import EntityTrait
from core.models import Teasurer, Cashier

TYPE_CHOICES = [
    ('OUT', 'Retirada'),
    ('IN', 'Entrada'),
]

class FinancialTransaction(EntityTrait):
    justification = models.CharField(max_length=200)
    value = models.FloatField()
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    teasurer = models.ForeignKey(Teasurer, on_delete=models.CASCADE)
    cashier = models.ForeignKey(Cashier, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'financial_transacrtion'
        
    def __str__(self):
        return self.justification