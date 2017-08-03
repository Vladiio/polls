import string
import random

from django.utils.text import slugify


def generate_unique_string(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_unique_slug(instance, new_slug=None):
    cls_ = instance.__class__
    slug = slugify(instance.title) if new_slug is None else new_slug
    qs =cls_.objects.filter(slug=slug)
    if qs.exists():
        slug = slug + generate_unique_string()
        return generate_unique_slug(instance, slug)
    return slug
