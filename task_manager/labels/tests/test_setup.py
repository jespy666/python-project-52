from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Label
from task_manager.users.models import User
from task_manager.tasks.models import Task


class LabelTestCase(TestCase):
    fixtures = ['user.json', 'label.json', 'task.json']
    login_url = reverse_lazy('login')
    labels_url = reverse_lazy('labels')

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.task = Task.objects.get(pk=1)
        self.label = Label.objects.get(pk=1)
        self.client.force_login(self.user)
