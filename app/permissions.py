from rest_framework import permissions

class IsProjectMember(permissions.BasePermission):
    """
    Custom permission to only allow the creator or assignees of a project to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the requesting user is the creator or one of the assignees
        return request.user == obj.created_by or request.user in obj.assignees.all()
