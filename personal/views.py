from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse

from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'personal/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        pass
