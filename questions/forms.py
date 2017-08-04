from django import forms

from .models import Question, Answer


class CreateQuestionForm(forms.ModelForm):
    title = forms.CharField(help_text="Please, enter a title for your pool")
    answer = forms.CharField(required=False, help_text="Please, enter a new choice")

    class Meta:
        model = Question
        fields = ('title', 'answer')

