from rest_framework import permissions


class IsNonAuthenticated(permissions.BasePermission):
    message = 'Необходимо выйти из текущего аккаунта, прежде чем приступить к регистрации нового'

    def has_permission(self, request, view):
        return bool(not request.user.is_authenticated)


class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(request.user.is_author)
        except AttributeError:
            return False


class IsCurrentAuthorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        try:
            print(request.user, obj.author)
            return bool(request.user == obj.author)
        except AttributeError:
            return False
