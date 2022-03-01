from django.db import models
from datetime import datetime
from core.models import Member

class President(Member):
    startMandate = models.DateTimeField(default=datetime.now)
    endMandate = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'president'

    def __str__(self):
        return self.user.username