from rest_framework.permissions import BasePermission


class IsModer(BasePermission):

    def has_permission(self, request, view):

        if request.user.filter(groups='moders').exists():
            return True
        return False
