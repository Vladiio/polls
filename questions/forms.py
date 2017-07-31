from django import forms

from .models import Question


class CreateQuestionForm(forms.ModelForm):
    answer1 = forms.CharField()

    class Meta:
        model = Question
        fields = ('name',)
