from rest_framework import permissions
from assistants.models import Assistant

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

# class IsAssistant(permissions.BasePermission):
#     """
#     Custom permission to only allow non assistants to make an appointment.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#     # Write permissions are only allowed to the owner of the snippet.
#     assistant_list = Assistant.objects.filter(user = request.user)
#   if len(assistant_list) > 0:
#     if assistant_list.exists():
#
#     return obj.owner == request.user
