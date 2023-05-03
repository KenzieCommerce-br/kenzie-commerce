from rest_framework import permissions
from rest_framework.views import View


class IsVendorOrReadOnly(permissions.BasePermission):
    def has_permission(self, req, view: View) -> bool:
        if req.method in permissions.SAFE_METHODS:
            return True

        return req.user.is_authenticated and req.user.is_seller
