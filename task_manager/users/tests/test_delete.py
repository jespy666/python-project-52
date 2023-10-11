from .test_setup import UserTestCase
from django.urls import reverse_lazy
from ..models import User


class TestUserDelete(UserTestCase):

    def test_user_delete_yourself(self):
        response = self.client.post(reverse_lazy('delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.users_url)
        self.assertEqual(User.objects.count(), 1)

    def test_user_delete_unauthenticated(self):
        self.client.logout()
        response = self.client.post(reverse_lazy('delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertEqual(User.objects.count(), 2)

    def test_user_delete_another_user(self):
        response = self.client.post(reverse_lazy('delete', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.users_url)
        self.assertEqual(User.objects.count(), 2)
