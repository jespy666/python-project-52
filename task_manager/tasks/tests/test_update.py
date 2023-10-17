from django.urls import reverse_lazy

from .test_setup import TaskTestCase
from ...json_loader import load_json


class TestTaskUpdate(TaskTestCase):

    updated_cases = load_json('update_task.json')

    def test_update_success(self):
        response = self.client.post(
            reverse_lazy('task_update', kwargs={'pk': 1}),
            data=self.updated_cases['valid']
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.tasks_url)

    def test_update_success_with_flash(self):
        response = self.client.post(
            reverse_lazy('task_update', kwargs={'pk': 1}),
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
            'Task updated successfully'
        )
        self.assertTemplateUsed(
            response,
            'tasks/task_list.html'
        )

    def test_update_with_existed_name(self):
        response = self.client.post(
            reverse_lazy('task_update', kwargs={'pk': 1}),
            data=self.updated_cases['already_exists']
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.tasks_url)

    def test_update_unauthenticated(self):
        self.client.logout()
        response = self.client.post(
            reverse_lazy('task_update', kwargs={'pk': 1}),
            data=self.updated_cases['valid']
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
