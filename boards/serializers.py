from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Board, Task

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class CreateBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title']

class ListBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["description", "is_hidden", "is_done"]

class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["is_hidden"]


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["description", "creation_date"]


class OwnerTaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['board']
