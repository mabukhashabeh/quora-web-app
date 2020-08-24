from django.urls import path
from apps.user.api.views import CurrentUserAPIView

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user")
]