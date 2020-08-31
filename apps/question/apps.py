from django.apps import AppConfig


class QuestionConfig(AppConfig):
    name = 'apps.question'

    def ready(self):
        import apps.question.signals

