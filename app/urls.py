
from app.views import RandomNumbersView
from django.urls import path

urlpatterns = [
    path("random/", RandomNumbersView.as_view(), name="random_numbers")
]
