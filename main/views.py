from django.shortcuts import render
from django.views import generic

from main.models import Question


class IndexView(generic.ListView):
    model = Question


class DetailView(generic.DetailView):
    model = Question