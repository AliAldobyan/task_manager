from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import (RegisterSerializer, CreateBoardSerializer,
						ListBoardSerializer, TaskSerializer,
						UpdateTaskSerializer, OwnerTaskListSerializer, TaskListSerializer
						)
from .models import Board, Task
from .permissions import IsBoardOwner, IsTaskOwner

class Register(CreateAPIView):
	serializer_class = RegisterSerializer


class CreateBoard(CreateAPIView):
	serializer_class = CreateBoardSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class ListBoard(ListAPIView):
	queryset = Board.objects.all()
	serializer_class = 	ListBoardSerializer
	permission_classes = [IsAuthenticated]


class TaskListView(ListAPIView):
	filter_backends = [OrderingFilter]
	ordering_fields = ['creation_date', 'is_hidden', 'is_done']
	permission_classes = [IsTaskOwner]

	def get_queryset(self):
		return Task.objects.filter(board_id=self.kwargs['board_id'])

	def get_serializer_class(self):
		if self.request.user.is_staff:
			return  TaskListSerializer
		else:
			return OwnerTaskListSerializer



class AddTask(CreateAPIView):
	serializer_class = TaskSerializer
	permission_classes = [IsBoardOwner]

	def perform_create(self, serializer):
		serializer.save(board_id=self.kwargs['board_id'])


class UpdateTask(RetrieveUpdateAPIView):
	queryset = Task.objects.all()
	serializer_class = UpdateTaskSerializer
	permission_classes = [IsTaskOwner]
	lookup_field = 'id'
	lookup_url_kwarg = 'task_id'
