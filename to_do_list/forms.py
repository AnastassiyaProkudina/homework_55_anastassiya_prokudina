from django import forms
from django.core.exceptions import ValidationError

from to_do_list.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "status", "date_to_do", "description"]
        widgets = {
            'date_to_do': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее двух символов')
        return title
