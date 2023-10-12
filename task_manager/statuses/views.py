from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as trans
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Status
from .forms import StatusCreateForm, StatusUpdateForm
from ..mixins import UserAuthRequiredMixin


class StatusListView(UserAuthRequiredMixin, ListView):
    template_name = 'statuses/status_list.html'
    model = Status
    context_object_name = 'statuses'
    login_url = 'login'
    permission_denied_message = trans(
        'You must to be log in'
    )


class StatusCreateView(SuccessMessageMixin, UserAuthRequiredMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    success_url = reverse_lazy('statuses')
    template_name = 'statuses/create.html'
    login_url = 'login'
    success_message = trans('Status created successfully')
    permission_denied_message = trans(
        'You must to be log in'
    )


class StatusUpdateView(SuccessMessageMixin, UserAuthRequiredMixin, UpdateView):
    model = Status
    form_class = StatusUpdateForm
    success_url = reverse_lazy('statuses')
    template_name = 'statuses/create.html'
    login_url = 'login'
    success_message = trans('Status updated successfully')
    permission_denied_message = trans(
        'You must to be log in'
    )


class StatusDeleteView(SuccessMessageMixin, UserAuthRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    login_url = 'login'
    success_url = reverse_lazy('statuses')
    success_message = trans('Status successfully removed')
    permission_denied_message = trans(
        'You must to be log in'
    )
