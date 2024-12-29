from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwner(BasePermission):
    """
    仅允许对象的所有者访问。
    """

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user
