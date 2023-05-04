from django.urls import path
from .views import CartView, CartDetailView

urlpatterns = [
    path("cart/", CartView.as_view()),
    path("cart/<int:pk>/", CartDetailView.as_view()),
]
