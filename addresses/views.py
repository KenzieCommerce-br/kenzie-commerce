from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework_simplejwt import authentication
from users.models import User
from .models import Address
from .serializers import AddressSerializer
from users.permissions import IsOwnerOrAdminAddress


class AddressView(generics.CreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdminAddress]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        serializer.save(user=user)
