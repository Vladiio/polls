from django import forms

from .models import Question


class CreateQuestionForm(forms.ModelForm):
    answer = forms.CharField()

    class Meta:
        model = Question
        fields = ('name',)
