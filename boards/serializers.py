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

class CreateTaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ["description", "is_hidden", "is_done"]


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ["description", "creation_date", "is_done"]


class ListBoardSerializer(serializers.ModelSerializer):
	tasks = serializers.SerializerMethodField()
	owner = serializers.SerializerMethodField()
	class Meta:
		model = Board
		fields = ['title', 'owner', 'tasks']

	def get_tasks(self,obj):
		if self.context['request'].user == obj.owner:
			return TaskSerializer(Task.objects.filter(board=obj), many=True).data
		return  TaskSerializer(Task.objects.filter(board=obj, is_hidden=False), many=True).data
	def get_owner(self,obj):
		return obj.owner.first_name


class TaskListSerializer(serializers.ModelSerializer):
	tasks = serializers.SerializerMethodField()
	owner = serializers.SerializerMethodField()
	class Meta:
		model = Board
		fields = ["title", "owner", 'tasks']

	def get_tasks(self,obj):
		return TaskSerializer(Task.objects.filter(board=obj, is_hidden=False), many=True).data

	def get_owner(self,obj):
		return obj.owner.first_name


class OwnerTaskListSerializer(serializers.ModelSerializer):
	is_done = serializers.SerializerMethodField()
	not_done = serializers.SerializerMethodField()
	owner = serializers.SerializerMethodField()
	class Meta:
		model = Board
		fields = ['title', 'owner', 'is_done', 'not_done']

	def get_is_done(self, obj):
		return TaskSerializer(Task.objects.filter(board=obj, is_done=True), many=True).data

	def get_not_done(self, obj):
		return TaskSerializer(Task.objects.filter(board=obj, is_done=False), many=True).data

	def get_owner(self,obj):
		return obj.owner.first_name


class UpdateTaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ["is_hidden"]
