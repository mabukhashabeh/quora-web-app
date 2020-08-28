from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.api.permissions import IsAuthorOrReadOnly
from apps.api.serializers import QuestionSerializer
from apps.question.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet provide full crud mechanism
    for specific model
    """
    queryset = Question.objects.all()
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)