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
        return Question.objects.all()


class QuestionDetailView(LoginRequiredMixin, DetailView):

    def get_queryset(self):
        return Question.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        question = self.get_object()
        allow_vote = True
        allow_update = False
        user = self.request.user
        if not user.is_authenticated() or user in question.members.all():
            allow_vote = False
        context['allow_vote'] = allow_vote
        return context

    def post(self, request, *args, **kwargs):
        answer_id = request.POST.get('answer_id')
        question_slug = request.POST.get('question_slug')

        question = Question.objects.get(slug=question_slug)
        question.members.add(request.user)

        if answer_id:
            answer = Answer.objects.get(id=answer_id)
            answer.votes += 1
            answer.save()

        return redirect(reverse_lazy('questions:detail', kwargs={'slug': question_slug}))


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


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CreateQuestionForm
    model = Question
