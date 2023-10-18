from django_filters import FilterSet, BooleanFilter
from django.forms import CheckboxInput
from django.utils.translation import gettext as _
from .models import Task


class TaskFilter(FilterSet):

    only_my_tasks = BooleanFilter(
        label=_('Only my tasks'),
        widget=CheckboxInput(attrs={'class': 'form-check-input'}),
        method='filter_my_tasks',
    )

    def filter_my_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(task_performer=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = {
            'status': ['exact'],
            'task_performer': ['exact'],
            'label': ['exact'],
        }
        field_labels = {
            'status': _('Status'),
            'task_performer': _('Task Performer'),
            'label': _('Label'),
        }
