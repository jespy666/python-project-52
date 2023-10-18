from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.users.models import User
from ..models import Status


class StatusTestCase(TestCase):
    fixtures = ['status.json', 'user.json']
    login_url = reverse_lazy('login')
    statuses_url = reverse_lazy('statuses')

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.status = Status.objects.get(pk=1)
        self.client.force_login(self.user)
