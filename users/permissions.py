from rest_framework.permissions import BasePermission

class UserIsModeratorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()

class UserIsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff