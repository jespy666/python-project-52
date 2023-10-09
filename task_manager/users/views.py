from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CustomUserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import UserPermissionMixin


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


class UserUpdateView(LoginRequiredMixin, UserPermissionMixin,
                     UpdateView, SuccessMessageMixin):
    model = User
    template_name = 'users/create.html'
    form_class = CustomUserCreateForm

    success_url = reverse_lazy('users')
    success_message = 'User updated successfully'

    permission_message = 'You do not have permission to edit another user.'
    permission_url = reverse_lazy('users')

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'You need to be logged in to edit a profile.'
            )
            return redirect(reverse_lazy('login'))
        return super().handle_no_permission()


class UserDeleteView(LoginRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'

    success_url = reverse_lazy('users')
    success_message = 'User successfully removed'

    permission_message = 'You do not have permission to edit another profile.'
    permission_url = reverse_lazy('users')

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'You need to be logged in to edit a profile.'
            )
            return redirect(reverse_lazy('login'))
        return super().handle_no_permission()
