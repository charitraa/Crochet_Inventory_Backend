from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed

class LoginRequiredPermission(BasePermission):
    """
    Custom permission to return a specific message when the user is not authenticated.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            raise AuthenticationFailed(detail="Login first", code=401)
        return True


class IsSuperuserOrAdmin(BasePermission):
    """
    Custom permission to allow access only to superusers or staff.
    """
    def has_permission(self, request, view):
        if  request.user.is_superuser or request.user.is_staff :
            raise AuthenticationFailed(detail="You do not have permission to access", code=403)
