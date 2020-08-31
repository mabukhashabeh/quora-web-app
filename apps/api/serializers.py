from rest_framework import serializers
from apps.question.models import Answer, Question


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B, %d %Y")

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ["question", "likes", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B, %d %Y")

    def get_likes_count(self, instance):
        return instance.likes.count()

    def get_user_has_liked(self, instance):
        request = self.context.get("request")
        return instance.likes.filter(pk=request.user.pk).exists()


