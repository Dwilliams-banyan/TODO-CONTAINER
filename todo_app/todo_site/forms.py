from django.forms import ModelForm

from todo_site.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']