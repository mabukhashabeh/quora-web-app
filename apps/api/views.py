from rest_framework import viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.api.permissions import IsAuthorOrReadOnly
from apps.api.serializers import QuestionSerializer, AnswerSerializer
from apps.question.models import Question, Answer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet provide full crud
    for specific model
    """
    queryset = Question.objects.all()
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        question_slug = self.kwargs.get("question_slug")
        question = get_object_or_404(Question, slug=question_slug)

        if question.answers.filter(author=user).exists():
            raise ValidationError("You have already answered this Question!")

        serializer.save(author=user, question=question)


class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        question_slug = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug=question_slug)