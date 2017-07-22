from django.db import models
from django.utils.text import slugify


class Question(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100, unique=True)
    creation_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Answer(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.content