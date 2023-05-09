from django.urls import path
from . import views


urlpatterns = [
    # path('ratings/', views.RatingView.as_view()),
    # path('users/<int:user_id>/ratings/', views.RatingView.as_view()),
    path('users/<int:user_id>/ratings/<int:product_id>/', views.RatingView.as_view()),
]
