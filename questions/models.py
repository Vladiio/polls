from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save

from .utils import generate_unique_slug


class QuestionQuerySet(models.query.QuerySet):

    def search(self, query):
        if query:
            return self.filter(
                Q(title__iexact=query)|
                Q(title__icontains=query)
                ).distinct()
        return self


class QuestionManager(models.Manager):

    def get_queryset(self):
        return QuestionQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class Question(models.Model):
    title = models.CharField(max_length=100,
                             help_text="Please, enter a title for your pool")
    slug = models.SlugField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    total_votes = models.IntegerField(default=0)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     blank=True,
                                     related_name='completed_questions')

    objects = QuestionManager()

    class Meta:
        ordering = ('-updated', '-timestamp')

    def get_absolute_url(self):
        return reverse('questions:update-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=100,
                             help_text="Please, enter a new answer",
                             verbose_name="Answer")
    votes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='answer_picture', blank=True)

    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name="answers",
                                 blank=True)

    def __str__(self):
        return self.title


def question_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance)


pre_save.connect(question_pre_save_receiver, sender=Question)
