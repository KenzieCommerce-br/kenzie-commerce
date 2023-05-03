from django.urls import path
from . import views


urlpatterns = [
    path("users/<int:pk>/orders/", views.OrderView.as_view()),
]
