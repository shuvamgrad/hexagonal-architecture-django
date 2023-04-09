from rest_framework import serializers
from anapp.application.port.api.command.transaction_command import TransactionCommand


class MakeTransactionCommandDeserializer(serializers.Serializer[TransactionCommand]):
    transaction_id = serializers.UUIDField()
    user_id = serializers.UUIDField()
    amount = serializers.FloatField()

    def create(self):
        return TransactionCommand(**self.validated_data)