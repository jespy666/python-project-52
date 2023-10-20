from django.urls import reverse_lazy

from task_manager.test_setup import TaskManagerTestCase
from task_manager.json_loader import load_json


class TestLabelUpdate(TaskManagerTestCase):

    updated_cases = load_json('label/update.json')

    def test_update_success(self):
        response = self.client.post(
            reverse_lazy('label_update', kwargs={'pk': 1}),
            data=self.updated_cases['valid']
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.labels_url)

    def test_update_success_with_flash(self):
        response = self.client.post(
            reverse_lazy('label_update', kwargs={'pk': 1}),
            data=self.updated_cases['valid'],
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)

        message = messages[0]
        self.assertEqual(message.tags, 'success')
        self.assertEqual(
            message.message,
            'Label updated successfully'
        )
        self.assertTemplateUsed(
            response,
            'labels/label_list.html'
        )

    def test_update_with_existed_name(self):
        response = self.client.post(
            reverse_lazy('label_update', kwargs={'pk': 1}),
            data=self.updated_cases['already_exists']
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.labels_url)

    def test_update_unauthenticated(self):
        self.client.logout()
        response = self.client.post(
            reverse_lazy('label_update', kwargs={'pk': 1}),
            data=self.updated_cases['valid']
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)