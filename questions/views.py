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

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .models import Question, Answer
from .forms import CreateQuestionForm
from .serializers import QuestionSerializer, AnswerSerializer
from .permissions import IsOwnerOrReadOnlyQuestion, IsOwnerOrReadOnlyAnswer


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnlyQuestion)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return Question.objects.all()

    @detail_route(methods=['POST'])
    def answers(self, request, pk=None):
        obj = self.get_object()
        serializer = AnswerSerializer(data=request.data,
                                      context={'request': request})
        if serializer.is_valid():
            serializer.save(question=obj)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnlyAnswer)

    def get_queryset(self, *args, **kwargs):
        return Answer.objects.all()

    @detail_route(methods=["GET"])
    def vote(self, request, pk=None):
        obj = self.get_object()
        status = obj.make_vote(request.user)
        return Response({'status': status,
                         'votes': obj.votes,
                         'answer_id': obj.id})

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
                question.total_votes += 1
                question.save()

            return JsonResponse({"votes": answer.votes})


class QuestionListView(ListView):

    def get_queryset(self):
        return Question.objects.filter(is_active=True)[:5]

    def get_context_data(self, *args, **kwargs):
        header = "Popular"
        context = super().get_context_data(*args, **kwargs)
        qs = Question.objects.filter(is_active=True).order_by('-total_votes')
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


