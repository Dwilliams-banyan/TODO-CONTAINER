from django.forms import ModelForm

from todo_site.models import Task, Comment, Tag

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args, **kwargs)

        self.instance.task = task

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.task = kwargs.pop('task_object')
        super().__init__(*args, **kwargs)

        self.instance.task = self.task
        # self.fields['name'].label = ''

# Changes had to be made for the many to many relationship to be save
# Overide the save method
    def save(self, *args, **kwargs):
        tag = Tag.objects.create(name= self.data['name'])
        self.task.tags.add(tag)