from tracker import views
from django.urls import path, include

urlpatterns = [
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('create_task/', views.create_task, name='create_task'),
    path('my_task/', views.my_tasks, name='my_tasks'),
    path('task_detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('close_task/<int:pk>/', views.close_task, name='close_task'),
    path('shuffle_tasks/', views.shuffle_tasks, name='shuffle_tasks')
]
