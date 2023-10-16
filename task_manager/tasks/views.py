from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as t

from ..mixins import UserAuthRequiredMixin, TaskAuthorPermissionMixin
from .models import Task
from .filters import TaskFilter
from .forms import TaskCreateForm, TaskUpdateForm


class TasksListView(UserAuthRequiredMixin, FilterView):
    template_name = 'tasks/task_list.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    login_url = 'login'
    permission_denied_message = t('You must to be log in')


class TaskView(UserAuthRequiredMixin, DetailView):
    template_name = 'tasks/show.html'
    model = Task
    context_object_name = 'task'
    login_url = 'login'
    permission_denied_message = t('You must to be log in')


class TaskCreateView(UserAuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/create.html'
    login_url = 'login'
    success_message = t('Task created successfully')
    permission_denied_message = t('You must to be log in')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UserAuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/create.html'
    login_url = 'login'
    success_message = t('Task updated successfully')
    permission_denied_message = t('You must to be log in')


class TaskDeleteView(UserAuthRequiredMixin, SuccessMessageMixin,
                     TaskAuthorPermissionMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    login_url = 'login'
    success_url = reverse_lazy('tasks')
    success_message = t('Task successfully removed')
    permission_denied_message = t('You must to be log in')
    author_url = reverse_lazy('tasks')
    author_message = t('Only its author can delete a task')
