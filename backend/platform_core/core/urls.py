from django.urls import path
from . import views  # full import path

urlpatterns = [
    path("", views.index, name="index"),
    path("api/hello/", views.hello_world),
    path("contracts/", views.get_contracts),
    path("users/", views.get_users),
]
