from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView
        )

from .models import Question, Answer
from .forms import CreateQuestionForm


class QuestionListView(ListView):

    def get_queryset(self):
        return Question.objects.filter(is_active=True)


class QuestionUpdateView(DetailView):

    def get_queryset(self):
        return Question.objects.filter(is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        question = self.get_object()
        allow_vote = True
        user = self.request.user
        if not user.is_authenticated() or user in question.members.all():
            allow_vote = False
        context['allow_vote'] = allow_vote
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
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
