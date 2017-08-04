from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
        View,
        ListView,
        DetailView,
        CreateView,
        UpdateView
        )

from .models import Question, Answer
from .forms import CreateQuestionForm


class VoteView(View):

    def get(self, *args, **kwargs):
        if self.request.is_ajax():
            slug = self.kwargs.pop('slug')
            question = Question.objects.filter(slug=slug).first()
            answer_id = self.request.GET.get('answer_id', '')
            answer = question.answer_set.filter(id=answer_id).first()

            if self.request.user not in question.members.all():
                answer.votes += 1
                answer.save()
                question.members.add(self.request.user)

            return JsonResponse({"votes": answer.votes})


class QuestionListView(ListView):

    def get_queryset(self):
        return Question.objects.filter(is_active=True)



class QuestionDetailView(DetailView):

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
