from rest_framework import permissions
from django.contrib import auth

class IsNewUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.auth == None
        
