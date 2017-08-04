from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput,
                                                     label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                                     label="Password again")

    class Meta:
        model = User
        fields = ('username',)
