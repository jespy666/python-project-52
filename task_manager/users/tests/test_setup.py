from django.test import TestCase
from django.urls import reverse_lazy
from ..models import User


class UserTestCase(TestCase):
    fixtures = ['user.json']
    login_url = reverse_lazy('login')
    users_url = reverse_lazy('users')

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)
