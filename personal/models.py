from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from questions.utils import generate_unique_string as generate_code

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)

    def send_activation_email(self):
        if self.activated:
            pass
        else:
            self.activation_key = generate_code(size=10)
            self.save()
            path_ = reverse('activate', kwargs={'code': self.activation_key})
            subject = "Account activation"
            from_email = settings.DEFAULT_FROM_EMAIL
            body = f'To continue registration you need to activate your account: {path_}'
            recipient_list = [self.user.email]
            sent_email = send_mail(subject,
                                                     body,
                                                     from_email,
                                                     recipient_list,
                                                     fail_silently=False)


def post_save_user_receiver(sender, instance,
                                                created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)
