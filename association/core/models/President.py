from django.db import models
from datetime import datetime
from core.models import Member

class President(Member):
    startMandate = models.DateTimeField(default=datetime.now)
    endMandate = models.DateTimeField(null=True)

    class Meta:
        db_table = 'president'

    def __str__(self):
        return f"President {self.startMandate.strftime('%d/%m/Y%')} - {self.endMandate.strftime('%d/%m/Y%')}"