from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Questionnaire
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django.forms import modelformset_factory


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = '__all__'
        exclude = ['patient', 'date_time']