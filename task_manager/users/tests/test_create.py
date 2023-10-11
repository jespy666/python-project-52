from task_manager.json_loader import load_json
from .test_setup import UserTestCase
from django.urls import reverse_lazy


class TestUserCreate(UserTestCase):
    create_url = reverse_lazy('create')
    created_cases = load_json('create.json')

    def setUp(self):
        self.client.logout()

    def test_user_success_create(self):
        response = self.client.post(
            self.create_url,
            data=self.created_cases['valid']
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)

    def test_user_success_create_with_flash(self):
        response = self.client.post(
            self.create_url,
            data=self.created_cases['valid'],
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)

        message = messages[0]
        self.assertEqual(message.tags, 'success')
        self.assertEqual(
            message.message,
            'User created successfully'
        )
        self.assertTemplateUsed(response, 'login_form.html')

    def test_user_create_with_existed_username(self):
        response = self.client.post(
            self.create_url,
            data=self.created_cases['existed_username'],
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')
