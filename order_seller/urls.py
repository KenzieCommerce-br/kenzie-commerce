from django.urls import path
from . import views


urlpatterns = [
    path('seller/orders/<int:order_id>/', views.OrderSellerView.as_view()),
]
