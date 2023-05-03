from django.urls import path
from . import views


urlpatterns = [
    path("products/create", views.ProductView.as_view()),
    path("products/<int:pk>", views.DetailProductView.as_view()),
]
