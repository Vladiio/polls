from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.core.urlresolvers import reverse

from .forms import RegisterForm
from .models import Profile


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'personal/register.html'
    success_url = '/login/'


def activate_view(request, code=None):
    profile = get_object_or_404(Profile, activation_key=code)
    user_ = profile.user
    user_.is_active = True
    user_.save()
    profile.activated = True
    profile.activation_key = None
    profile.save()
    return redirect('/login/')
