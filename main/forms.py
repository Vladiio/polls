from django import forms

from main import models


class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = models.Qustion
