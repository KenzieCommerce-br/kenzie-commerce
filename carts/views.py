from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from products.models import Product


from .serializers import CartItemSerializer, CartSerializer

from .models import Cart, CartItem


class CartView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        return serializer.save(user_id=int(self.request.user.id))


class CartDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
