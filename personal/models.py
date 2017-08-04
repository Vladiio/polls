from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail

from questions.utils import generate_unique_slug as generate_code

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)

    def send_activation_email(self):
        print("Sending...")


def post_save_user_receiver(sender, instance,
                                                created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)
