from django.forms import ModelForm
from .models import Task


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'task_performer',
        )


class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'task_performer',
        )

    def clean_name(self):
        return self.cleaned_data.get('name')
