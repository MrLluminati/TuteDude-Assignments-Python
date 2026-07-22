from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "You can only access your own posts."

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
