from rest_framework import permissions

class IsPostOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST" and obj.customer.user == request.user:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return obj.customer.user == request.user

class IsImageOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST" and obj.post.customer.user == request.user:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return obj.post.customer.user == request.user