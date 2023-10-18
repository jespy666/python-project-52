from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext as _

from ..mixins import UserAuthRequiredMixin, ObjectDeleteProtectionMixin
from .models import Label
from .forms import LabelCreateForm, LabelUpdateForm


class LabelListView(UserAuthRequiredMixin, ListView):
    template_name = 'labels/label_list.html'
    model = Label
    context_object_name = 'labels'
    login_url = 'login'
    permission_denied_message = _('You must to be log in')


class LabelCreateView(UserAuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    success_url = reverse_lazy('labels')
    template_name = 'labels/create.html'
    login_url = 'login'
    success_message = _('Label created successfully')
    permission_denied_message = _('You must to be log in')


class LabelUpdateView(UserAuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelUpdateForm
    success_url = reverse_lazy('labels')
    template_name = 'labels/update.html'
    login_url = 'login'
    success_message = _('Label updated successfully')
    permission_denied_message = _('You must to be log in')


class LabelDeleteView(UserAuthRequiredMixin, ObjectDeleteProtectionMixin,
                      SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    login_url = 'login'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully removed')
    permission_denied_message = _('You must to be log in')
    protection_message = _('Cannot delete label because it is in use')
    protected_url = reverse_lazy('labels')
