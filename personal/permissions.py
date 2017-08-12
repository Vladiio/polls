from rest_framework import permissions


class RegisterPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id or request.user.is_superuser

    def has_permission(self, request, view):
        return request.user.is_authenticated or request.user.is_superuser
