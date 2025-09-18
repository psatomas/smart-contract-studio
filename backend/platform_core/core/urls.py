from django.urls import path
from . import views  # full import path

urlpatterns = [
    path("", views.index, name="index"),
]
