from django.db import models
from ._EntityTrait import EntityTrait
from django.contrib.auth.models import User
from core.models import Vehicle

class Member(EntityTrait):
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    cep = models.CharField(max_length=200, blank=True)
    number = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'member'
        ordering = ['street', 'city', 'state', 'cep', 'number']

    def __str__(self):
        return self.user.username