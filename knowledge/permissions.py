from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user

class IsContainerOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsContainerPrivateOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_private:
            return obj.owner == request.user
        return True