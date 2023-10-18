from django.forms import ModelForm
from .models import Label


class LabelCreateForm(ModelForm):
    class Meta:
        model = Label
        fields = ('name',)


class LabelUpdateForm(ModelForm):
    class Meta:
        model = Label
        fields = ('name',)

    def clean_name(self):
        return self.cleaned_data.get('name')
