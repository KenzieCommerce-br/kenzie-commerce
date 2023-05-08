from django.urls import path
from . import views


urlpatterns = [
    path('users/<int:user_id>/orders/', views.OrderView.as_view()),
    path('users/<int:user_id>/orders/<int:order_id>/', views.OrderDetailView.as_view()),
]
