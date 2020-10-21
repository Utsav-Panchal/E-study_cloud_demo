from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse

from ..base.views import BaseUpdateView
from .forms import UserProfileForm
from app_modules.core_apps.users.models import User


class UserProfileSettingView(BaseUpdateView):
    """
    This is the generic view to update user profile detail.
    It extends with BaseUpdateView to check permission.
    Override get_object() to get logged in user and
    get_success_url() to get url for redirect after success response.
    """

    model = User
    template_name = "webapp/users/profile.html"
    permission_required = "users.change_user"
    form_class = UserProfileForm

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse("webapp:users:user-settings", kwargs=self.kwargs)
