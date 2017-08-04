from django.shortcuts import render, redirect, get_object_or_404
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
            question = get_object_or_404(Question, slug=slug)
            answer_id = self.request.GET.get('answer_id', '')
            answer = question.answer_set.filter(id=answer_id).first()

            if self.request.user not in question.members.all():
                answer.votes += 1
                answer.save()
                question.members.add(self.request.user)

            return JsonResponse({"votes": answer.votes})


class QuestionListView(ListView):

    def get_queryset(self):
        return Question.objects.filter(is_active=True)[:5]

    def get_context_data(self, *args, **kwargs):
        header = "Popular"
        context = super().get_context_data(*args, **kwargs)
        qs = Question.objects.filter(is_active=True).order_by('-members')
        query = self.request.GET.get('query')
        qs = qs.search(query)

        context['popular_object_list'] = qs[:5]
        context['header'] = header
        return context


class QuestionUpdateDetailView(UpdateView):
    form_class = CreateQuestionForm
    template_name = 'questions/update-detail.html'

    def get_queryset(self):
        return Question.objects.filter(is_active=True)

    def get_context_data(self, *args, **kwargs):
        allow_vote = True
        allow_edit = False

        context = super().get_context_data(*args, **kwargs)
        question = self.get_object()
        user = self.request.user

        if user in question.members.all():
            allow_vote = False
        if user.id == question.author.id:
            allow_edit = True

        context['allow_vote'] = allow_vote
        context['allow_edit'] = allow_edit
        return context

    def form_valid(self, form):
        obj = self.get_object()
        new_answer = form.cleaned_data.get('answer')
        if new_answer:
            new_answer = Answer.objects.create(title=new_answer,
                                                                          question=obj)
            new_answer.save()
        return super().form_valid(form)


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ('title',)

    def form_valid(self, form):
        question = form.save(commit=False)
        question.author = self.request.user
        question.save()
        return super().form_valid(form)
