from django.db import models
from core.models import Member

class Partner(Member):
    canUseVehicle = models.BooleanField(default=False)
    montlyValue = models.FloatField()
    message = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'partner'

    def __str__(self):
        return self.user.username