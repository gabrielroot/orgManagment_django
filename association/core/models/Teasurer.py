from django.db import models
from core.models import Member

class Teasurer(Member):
    canWithDraw = models.BooleanField(default=False)

    class Meta:
        db_table = 'teasurer'

    def __str__(self):
        return self.user.username