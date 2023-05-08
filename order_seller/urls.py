from django.urls import path
from . import views


urlpatterns = [
    path('seller/orders/<int:order_id>/', views.OrderSellerView.as_view()),
    path('seller/<int:seller_id>/orders/pending/', views.OrderSellerPendingView.as_view()),
    path('seller/<int:seller_id>/orders/finished/', views.OrderSellerFinishedView.as_view()),
]
