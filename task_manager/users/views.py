from django.urls import reverse_lazy
from .models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CustomUserCreateForm


class UserListView(ListView):
    template_name = 'users/users.html'
    model = User
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'users/create.html'


class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'users/create.html'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
