from django.urls import path
from todo_site.views import HomeView, TaskDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('todo/<int:task_id>', TaskDetailView.as_view(), name='task_detail'),
]