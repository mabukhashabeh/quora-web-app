from django.db import models
from django.conf import settings

from base.models import BaseModel

User = settings.AUTH_USER_MODEL


class Question(BaseModel):
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    def __str__(self):
        return self.content


class Answer(BaseModel):

    body = models.TextField()
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    voters = models.ManyToManyField(
        User,
        related_name="votes"
    )

    def __str__(self):
        return self.author.username
