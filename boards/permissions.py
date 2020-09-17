from rest_framework.permissions import BasePermission


class IsBoardOwner(BasePermission):
	message = "you must be the board owner!"

	def has_object_permission(self, request, view, obj):
		if (obj.owner == request.user):
			return True
		else:
			return False
