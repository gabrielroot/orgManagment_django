from django.db import models
from datetime import datetime

class EntityTrait(models.Model):

    createdAt = models.DateTimeField(default=datetime.now)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True)
    
    class Meta:
        abstract = True