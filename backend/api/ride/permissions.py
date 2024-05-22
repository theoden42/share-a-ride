from rest_framework import permissions


class IsRideOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_initiator.user.id == request.user.id
