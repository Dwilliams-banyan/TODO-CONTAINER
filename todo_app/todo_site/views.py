from django.shortcuts import redirect, render

# Create your views here.
from django.views import View

from todo_site.models import Task
from todo_site.forms import TaskForm

class HomeView(View):
    def get(self, request):
        tasks = Task.objects.all()
        task_form = TaskForm()

        html_data = {
            'task_list': tasks,
            'form': task_form
        }
        return render (
            request,
            'index.html',
            context = html_data
        )

    def post(self, request):
        task_form = TaskForm(request.POST)
        task_form.save()

        return redirect('home')


class TaskDetailView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)

        return render(request, 'detail.html', context ={'task_object': task, 'form': task_form})

    def post(self, request, task_id):

        task = Task.objects.get(id=task_id)
        print(request.POST)
        
        if 'update' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()

        # task = Task.objects.get(id=task_id)
        # task_form = TaskForm(request.POST, instance=task)
        # task_form.save()

        return redirect('home')



