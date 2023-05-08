from rest_framework import permissions, views
from .models import Order


class IsClientOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view: views.View, obj: Order) -> bool:
        return (
            request.user.is_authenticated
            and obj.user == request.user
            or request.user.is_admin
        )
