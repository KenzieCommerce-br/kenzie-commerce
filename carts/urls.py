from django.urls import path
from .views import CartView, FinalizeOrderView

urlpatterns = [
    path("cart/", CartView.as_view()),
    path("cart/finalize_order/", FinalizeOrderView.as_view()),
]
