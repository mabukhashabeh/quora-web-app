from django.contrib import admin
from apps.question.models import Answer, Question

admin.site.register(Answer)
admin.site.register(Question)