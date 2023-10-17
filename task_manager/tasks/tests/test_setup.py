from django.test import TestCase
from django.urls import reverse_lazy

from task_manager.users.models import User
from task_manager.statuses.models import Status
from ..models import Task


class TaskTestCase(TestCase):
    fixtures = ['task.json', 'user.json', 'status.json']
    login_url = reverse_lazy('login')
    tasks_url = reverse_lazy('tasks')

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.status = Status.objects.get(pk=1)
        self.task = Task.objects.get(pk=1)
        self.client.force_login(self.user)
