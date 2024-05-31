from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_task/<int:task_id>/', views.delete, name='delete_task'),
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name='mark_as_done'),
]
