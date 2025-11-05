from django.urls import path
from .views import (
    HealthCheckView,
    BlockchainEventReceiveView,
    ContractListView,
    TransactionListView,
)

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health'),
    path('blockchain-data/', BlockchainEventReceiveView.as_view(), name='receive_blockchain_data'),
    path('contracts/', ContractListView.as_view(), name='contracts'),
    path('transactions/', TransactionListView.as_view(), name='transactions'),
]
