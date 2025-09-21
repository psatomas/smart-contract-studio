from django.urls import path
from . import views 
from .views import get_users, get_transactions
from .views import receive_blockchain_data

urlpatterns = [
    path("", views.index, name="index"),
    path("api/hello/", views.hello_world),
    path("contracts/", views.get_contracts),
    path("users/", views.get_users),
    path("transactions/", views.get_transactions),
    path("blockchain-data/", receive_blockchain_data, name="blockchain-data"),
]
