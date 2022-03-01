from django.db import models
from ._EntityTrait import EntityTrait
from core.models import Partner, President

STATUS_CHOICES = [
    ('CONCLUDED', 'Concluído'),
    ('PENDING', 'Pendente'),
    ('REFUSED', 'Recusado')
]

class Request(EntityTrait):
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    president = models.ForeignKey(President, blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        db_table = 'request'
        
    def __str__(self):
        return self.message