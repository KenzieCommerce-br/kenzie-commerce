from django.urls import path
from . import views


urlpatterns = [
    path("products/create", views.ProductView.as_view()),
]
