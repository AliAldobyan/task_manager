from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import RegisterSerializer, CreateBoardSerializer, ListBoardSerializer, TaskSerializer, UpdateTaskSerializer
from .models import Board, Task
from .permissions import IsBoardOwner

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


class AddTask(CreateAPIView):
	serializer_class = TaskSerializer
	permission_classes = [IsBoardOwner]
	lookup_field = 'id'
	lookup_url_kwarg = 'board_id'

class UpdateTask(RetrieveUpdateAPIView):
	serializer_class = UpdateTaskSerializer
	permission_classes = [IsBoardOwner]
	lookup_field = 'id'
	lookup_url_kwarg = 'task_id'
