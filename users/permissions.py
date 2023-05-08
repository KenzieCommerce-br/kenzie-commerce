from rest_framework import permissions
from .models import User
from products.models import Product
from rest_framework.views import Request, View


class IsOwnerOnlyOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return obj == request.user or request.user.is_superuser


class IsOwnerOrAdminAddress(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        user_id = view.kwargs.get("pk", False)
        return request.user.is_superuser or request.user.id == user_id


class IsVendorAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view: View) -> bool:
        if req.method in permissions.SAFE_METHODS:
            return True
        return req.user.is_seller or req.user.is_superuser


class IsSellerAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Product) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.user_id or request.user.is_superuser
