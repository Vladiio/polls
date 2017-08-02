from django import forms

from .models import Question, Answer


class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        obj = kwargs.pop('instance')
        count = 1
        for answer in obj.answer_set.all():
            name = f'answer{count}'
            self.fields[name] = forms.CharField()
            count += 1
