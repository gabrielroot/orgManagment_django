from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):

    
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    cep = models.CharField(max_length=200, blank=True)
    number = models.IntegerField(default=0)

    class Meta:
        db_table = 'member'
        ordering = ['street', 'city', 'state', 'cep', 'number']

    def __str__(self):
        return self.user.username