# Generated by Django 4.2 on 2023-04-07 12:23

import anapp.application.adapter.spi.persistence.entity.transactions_entity
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserTransactionEntity",
            fields=[
                (
                    "user_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("balance", models.FloatField()),
            ],
            options={
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="TransactionsEntity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("user_id", models.UUIDField()),
                ("transaction_id", models.UUIDField()),
                (
                    "amount",
                    models.FloatField(
                        validators=[
                            anapp.application.adapter.spi.persistence.entity.transactions_entity.validate_amount
                        ]
                    ),
                ),
            ],
            options={
                "db_table": "all_transactions",
                "unique_together": {("user_id", "transaction_id")},
            },
        ),
    ]
