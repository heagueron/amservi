# services/permissions.py
from rest_framework import permissions


class IsClientOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.client == request.user


"""
Django Rest Framework gives us several options for setting permissions: 
at a project-level, view level, or object level. Here, In we implement 
the last option and create a custom permission we can add to our 
OrderDetail view class.
"""