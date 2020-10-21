from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "app_modules.core_apps.users"
    verbose_name = _("Users")
