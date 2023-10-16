from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as t


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login_form.html'
    next_page = reverse_lazy('home')
    success_message = t('You are login in')


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('home')
    success_message = t('You are logout')

    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, self.success_message)
        return super().dispatch(request, *args, **kwargs)
