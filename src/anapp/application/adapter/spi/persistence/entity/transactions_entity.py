from __future__ import annotations
from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError

def validate_amount(amount):
    if amount <= 0:
        raise ValidationError("Amount Cannot be less than ZERO")
    return amount

class TransactionsEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.UUIDField()
    transaction_id = models.UUIDField()
    amount = models.FloatField(validators=[validate_amount])

    class Meta:
        unique_together = [['user_id', 'transaction_id']]
        db_table = 'all_transactions'