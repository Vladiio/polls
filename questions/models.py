from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                                                    blank=True,
                                                                    related_name='completed_questions')

    def get_absolute_url(self):
        return reverse('questions:detail-update', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='answer_picture', blank=True)

    question = models.ForeignKey(Question,
                                                       on_delete=models.CASCADE)

    def __str__(self):
        return self.title
