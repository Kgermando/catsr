import random
import string
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titre_bulletin)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def unique_slug_generator_formation(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titre_formation)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_event(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titre_evenement)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randomstr}".format(
            slug=slug,
            randomstr=random_string_generator(size=4),
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug