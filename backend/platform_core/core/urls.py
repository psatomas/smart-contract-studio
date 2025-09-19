from django.urls import path
from . import views 
from .views import get_users, get_transactions

urlpatterns = [
    path("", views.index, name="index"),
    path("api/hello/", views.hello_world),
    path("contracts/", views.get_contracts),
    path("users/", views.get_users),
    path("transactions/", views.get_transactions), 
]
