from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import (RegisterSerializer, CreateBoardSerializer,
						ListBoardSerializer, OwnerTaskListSerializer, TaskSerializer,
						UpdateTaskSerializer, TaskListSerializer
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
	ordering_fields = ['creation_date']
	permission_classes = [IsTaskOwner]


	def get_queryset(self):
		return Board.objects.filter(id=self.kwargs['board_id'])

	def get_serializer_class(self):
		board_obj = Board.objects.get(id=self.kwargs['board_id'])
		if self.request.user == board_obj.owner:
			return OwnerTaskListSerializer
		else:
			return TaskListSerializer



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


class DeleteTask(DestroyAPIView):
	queryset = Task.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'task_id'
	permission_classes = [IsTaskOwner]


class DeleteBoard(DestroyAPIView):
	queryset = Board.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'board_id'
	permission_classes = [IsBoardOwner]
