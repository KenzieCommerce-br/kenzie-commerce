from django.urls import path
from . import views


urlpatterns = [
    path("users/<int:pk>/address/", views.AddressCreateView.as_view()),
    path("users/<int:pk>/address-update/<int:id>/", views.AddressUpdateView.as_view()),
]
