"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django_registration.backends.one_step.views import RegistrationView

from apps.common.views import IndexTemplateView
from apps.user.forms import CustomUserForm
from project.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL

# https://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [
    path('admin/', admin.site.urls),

    path("accounts/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/",
         ),
         name="django_registration_register"
         ),

    path("accounts/", include("django_registration.backends.one_step.urls")),

    path("accounts/", include("django.contrib.auth.urls")),

    path("api-auth/", include("rest_framework.urls")),

    path("api/rest-auth/", include("rest_auth.urls")),

    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),

    path("api/", include("apps.api.urls")),

    path("api/user", include("apps.api.user.urls")),

    path("", IndexTemplateView.as_view(), name="entry-point")

]
