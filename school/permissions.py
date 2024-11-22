from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        return view.owner == request.user
