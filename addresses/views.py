from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework_simplejwt import authentication
from users.models import User
from .models import Address
from .serializers import AddressSerializer


class AddressView(generics.CreateAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        serializer.save(user=user)
