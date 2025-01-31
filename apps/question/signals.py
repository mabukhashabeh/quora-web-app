from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from base.utils import generate_random_string
from apps.question.models import Question


@receiver(pre_save, sender=Question)
def add_slug_to_question(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        content = instance.content[:20]
        slug = slugify(content)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string