from django import forms

from main import models


class CreateQuestionForm(forms.ModelForm):
    answer = forms.CharField()

    class Meta:
        model = models.Question
        fields = ('name',)
