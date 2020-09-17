"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from boards import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', TokenObtainPairView.as_view(), name='api-login'),
    path('register/', views.Register.as_view(), name='api-register'),


    path('create/', views.CreateBoard.as_view(), name='api-create'),
    path('boards/', views.ListBoard.as_view(), name='api-board'),
    path('tasks/<int:board_id>/', views.TaskListView.as_view(), name='api-task-list'),
    path('task/create/<int:board_id>/', views.AddTask.as_view(), name='api-add-task'),
    path('task/update/<int:task_id>/', views.UpdateTask.as_view(), name='api-update-task'),

]
