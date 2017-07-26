from django.shortcuts import render
from django.views import generic
from django.views.generic import edit
from django.urls import reverse_lazy

from main import models
from main import forms


class IndexView(generic.ListView):
    model = models.Question


class DetailView(generic.DetailView):
    model = models.Question


class QuestionCreate(edit.CreateView):
    form_class = forms.CreateQuestionForm
    template_name = "main/question_form.html"

    def form_valid(self, form):
        answer = form.cleaned_data.get('answer')
        question = form.save()
        new_answer = models.Answer.objects.create(content=answer,
                                                  question=question)
        new_answer.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        return context



class QuestionEdit(edit.UpdateView):
    form_class = forms.CreateQuestionForm

