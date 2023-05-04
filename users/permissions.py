from rest_framework import permissions
from .models import User
from rest_framework.views import Request, View


class IsOwnerOnlyOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return obj == request.user or request.user.is_superuser


class IsVendorOrReadOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view: View) -> bool:
        if req.method in permissions.SAFE_METHODS:
            return True
        return req.user.is_seller


class ReadOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view: View) -> bool:
        if req.method in permissions.SAFE_METHODS:
            return True
