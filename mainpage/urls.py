from .views import main_banner
from django.urls import path

urlpatterns = [
    path("", main_banner),
]

