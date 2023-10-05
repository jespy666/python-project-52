from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(LoginView):
    template_name = 'login_form.html'
    authentication_form = AuthenticationForm


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
