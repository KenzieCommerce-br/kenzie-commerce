from django.urls import path
from . import views


urlpatterns = [
    path("users/address/<int:pk>/", views.AddressView.as_view()),
]
