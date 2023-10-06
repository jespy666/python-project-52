from django.contrib import messages
from django.urls import reverse_lazy
from .models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CustomUserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin


class UserListView(ListView):
    template_name = 'users/users.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'users/create.html'
    success_message = 'User created successfully'


class UserUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('users')
    template_name = 'users/create.html'
    success_message = 'User successfully updated'

    def get_object(self, queryset=None):

        return self.request.user

    def test_func(self):
        user = self.get_object()
        print(user)
        print(self.request.user)
        if self.request.user == user:
            return True
        else:
            messages.error(
                self.request,
                'You do not have permission to change another user'
            )
            return False


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = 'User successfully removed'
