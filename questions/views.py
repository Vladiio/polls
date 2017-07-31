from django.shortcuts import render
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView
        )

from .models import Question, Answer
from .forms import CreateQuestionForm


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question


class QuestionCreateView(CreateView):
    form_class = CreateQuestionForm
    template_name = "main/question_form.html"

    def form_valid(self, form):
        answer = form.cleaned_data.get('answer')
        question = form.save()
        new_answer = Answer.objects.create(content=answer,
                                                                      question=question)
        new_answer.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        return context


class QuestionUpdateView(UpdateView):
    form_class = CreateQuestionForm

