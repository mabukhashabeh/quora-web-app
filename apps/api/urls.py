from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api import views

router = DefaultRouter()
router.register(r"questions", views.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("questions/<slug:question_slug>/answers/",
         views.AnswerListAPIView.as_view(),
         name="answer-list"),

    path("questions/<slug:question_slug>/answer/",
         views.AnswerCreateAPIView.as_view(),
         name="answer-create"),

    path("answers/<int:pk>/",
         views.AnswerReadUpdateDeleteAPIView.as_view(),
         name="answer-detail"),

    path("answers/<int:pk>/like/",
         views.AnswerLikeAPIView.as_view(),
         name="answer-like")
]