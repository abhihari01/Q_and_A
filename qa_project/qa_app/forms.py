from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'content')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)
