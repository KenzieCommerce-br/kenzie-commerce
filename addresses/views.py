from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response
from rest_framework_simplejwt import authentication
from .models import Address
from users import models, permissions as permissions_user
from .serializers import AddressSerializer, AddressUpdateSerializer


class AddressCreateView(generics.CreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions_user.IsOwnerOrAdminAddress]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):

        user = get_object_or_404(models.User, pk=self.kwargs['pk'])
        addresses_user = Address.objects.filter(user=user)

        for address in addresses_user:
            if address.default:
                setattr(address, 'default', False)
                address.save()
        serializer.save(user=user)


class AddressUpdateView(generics.UpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions_user.IsOwnerOrAdminAddress]

    queryset = Address.objects.all()
    serializer_class = AddressUpdateSerializer
    lookup_field = 'id'

    def remove_default(self):

        user = get_object_or_404(models.User, pk=self.kwargs['pk'])
        addresses_user = Address.objects.filter(user=user)

        for address in addresses_user:
            if address.default:
                setattr(address, 'default', False)
                address.save()

    def update(self, request, *args, **kwargs):

        if request.data['default'] is True:
            self.remove_default()

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return response.Response(serializer.data)
