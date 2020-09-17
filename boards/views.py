from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import RegisterSerializer, CreateBoardSerializer

class Register(CreateAPIView):
	serializer_class = RegisterSerializer


class CreateBoard(CreateAPIView):
    serializer_class = CreateBoardSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
