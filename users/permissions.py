from rest_framework import permissions
from .models import User
from rest_framework.views import Request, View


class IsOwnerOnlyOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return (
            obj == request.user or
            request.user.is_superuser
        )
