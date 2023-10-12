from .test_setup import StatusTestCase
from ..models import Status
from django.urls import reverse_lazy


class TestStatusDelete(StatusTestCase):

    def test_status_delete_success(self):
        response = self.client.post(
            reverse_lazy('status_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.statuses_url)
        self.assertEqual(Status.objects.count(), 0)

    def test_status_delete_success_with_flash(self):
        response = self.client.post(
            reverse_lazy('status_delete', kwargs={'pk': 1}),
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)

        message = messages[0]
        self.assertEqual(message.tags, 'success')
        self.assertEqual(
            message.message,
            'Status successfully removed'
        )
        self.assertTemplateUsed(
            response,
            'statuses/status_list.html'
        )

    def test_delete_unauthenticated(self):
        self.client.logout()
        response = self.client.post(
            reverse_lazy('status_delete', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertEqual(Status.objects.count(), 1)
