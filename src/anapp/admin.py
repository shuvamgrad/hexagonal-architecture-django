from django.contrib import admin
from .models import UserTransactionEntity, TransactionsEntity

admin.site.register(UserTransactionEntity)
admin.site.register(TransactionsEntity)