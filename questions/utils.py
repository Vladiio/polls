import string
import random

from django.utils.text import slugify


DONT_USE = ('create',)

def generate_unique_string(size=5, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_unique_slug(instance, new_slug=None):
    cls_ = instance.__class__
    slug = slugify(instance.title) if new_slug is None else new_slug
    is_exists =cls_.objects.filter(slug=slug).exists()
    if is_exists or slug in DONT_USE:
        random_string = generate_unique_string()
        slug = f"{slug}-{random_string}"
        return generate_unique_slug(instance, slug)
    print(slug)
    return slug
