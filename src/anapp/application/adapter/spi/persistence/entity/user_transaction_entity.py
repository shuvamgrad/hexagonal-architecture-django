from __future__ import annotations
from uuid import uuid4

from django.db import models

class UserTransactionEntity(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    balance = models.FloatField()

    class Meta:
        db_table = 'users'