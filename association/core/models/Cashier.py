from django.db import models

class Cashier(models.Model):
    
    balance = models.FloatField()
    
    class Meta:
        ordering = ["balance"]
        db_table = 'cashier'