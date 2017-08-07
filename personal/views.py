from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.core.urlresolvers import reverse

from .forms import RegisterForm
from .models import Profile


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'personal/register.html'
    success_url = '/login/'


def activate_view(request, code):
    profile = get_object_or_404(Profile, code=code)
    profile.user.is_active = True
    profile.activated = True
    profile.save()
