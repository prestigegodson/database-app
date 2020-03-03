from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Checks if user has permission to update on profile"""

    def has_object_permission(self, request, view, obj):
        """checks if user can update profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.id
