from rest_framework.permissions import BasePermission


class IsBoardOwner(BasePermission):
	message = "you must be the board owner!"

	def has_object_permission(self, request, view, obj):
		if (obj.owner == request.user):
			return True
		else:
			return False


class IsTaskOwner(BasePermission):
	message = "you must be the Task owner!"

	def has_object_permission(self, request, view, obj):
		if obj.board.owner == request.user:
			return True
		else:
			return False
