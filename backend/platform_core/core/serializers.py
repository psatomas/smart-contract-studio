from rest_framework import serializers
from .models import BlockchainEvent

class BlockchainEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockchainEvent
        fields = ["tx_hash", "value", "contract_address", "timestamp"]