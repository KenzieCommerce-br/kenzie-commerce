from django.urls import path
from . import views


urlpatterns = [
    path("procuts/create", views.ProductView.as_view()),
]
