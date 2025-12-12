from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of a note to edit/delete it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return getattr(obj, 'owner', None) == request.user
