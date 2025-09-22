from django.db import models

class BlockchainEvent(models.Model):
    tx_hash = models.CharField(max_length=66)
    value = models.DecimalField(max_digits=20, decimal_places=8)
    contract_address = models.CharField(max_length=42)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tx_hash} @ {self.contract_address}"

# Create your models here.
