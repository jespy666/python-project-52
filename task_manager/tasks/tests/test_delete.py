from .test_setup import TaskTestCase
from ..models import Task
from django.urls import reverse_lazy


class TestTaskDelete(TaskTestCase):

    def test_status_delete_success(self):
        response = self.client.post(
            reverse_lazy('task_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.tasks_url)
        self.assertEqual(Task.objects.count(), 0)

    def test_status_delete_success_with_flash(self):
        response = self.client.post(
            reverse_lazy('task_delete', kwargs={'pk': 1}),
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)

        message = messages[0]
        self.assertEqual(message.tags, 'success')
        self.assertEqual(
            message.message,
            'Task successfully removed'
        )
        self.assertTemplateUsed(
            response,
            'tasks/task_list.html'
        )

    def test_delete_unauthenticated(self):
        self.client.logout()
        response = self.client.post(
            reverse_lazy('task_delete', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertEqual(Task.objects.count(), 1)
