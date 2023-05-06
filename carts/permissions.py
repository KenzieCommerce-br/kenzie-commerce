from rest_framework import permissions
from .models import Cart
from rest_framework.views import View


class IsClientOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Cart) -> bool:
        return (
            request.user.is_authenticated
            and obj == request.user
            or request.user.is_admin
        )
