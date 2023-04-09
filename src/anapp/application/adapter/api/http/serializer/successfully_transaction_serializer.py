from rest_framework import serializers
from anapp.application.domain.model.transaction_result import SuccessfulTransactionResult

class SuccessfullyTransactionSerializer(serializers.Serializer[SuccessfulTransactionResult]):
    user_id = serializers.UUIDField()
    transaction_id = serializers.UUIDField()
    amount = serializers.FloatField()

