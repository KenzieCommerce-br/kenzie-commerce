from django.shortcuts import get_object_or_404
from rest_framework_simplejwt import authentication
from rest_framework import generics, permissions
from users.models import User
from .models import Order
from .serializers import OrderSerializer

class OrderView(generics.ListCreateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        serializer.save(user=user)
