from django.urls import path
from . import views  # full import path

urlpatterns = [
    path("", views.index, name="index"),
    path('hello/', views.hello_world),
]
