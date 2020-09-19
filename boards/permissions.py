from rest_framework.permissions import BasePermission


class IsBoardOwner(BasePermission):
	message = "you must be the board owner!"

	def has_object_permission(self, request, view, obj):
		return (obj.owner == request.user)


class IsTaskOwner(BasePermission):
	message = "you must be the Task owner!"

	def has_object_permission(self, request, view, obj):
		return (obj.board.owner == request.user)
