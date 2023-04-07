from django import forms
from django.contrib.auth import get_user_model

from .models import Questionnaire

User = get_user_model()


class PostForm(forms.ModelForm):

    class Meta:
        model = Questionnaire
        fields = ('description', 'location', 'price')
        labels = {'description': 'Описание', 'location': 'Локация', 'price': 'цена'}

    def clean_text(self):
        data = self.cleaned_data['description']
        if Questionnaire.description == '':
            raise forms.ValidationError(
                'Поле, текст обязателен для заполнения!')
        return data