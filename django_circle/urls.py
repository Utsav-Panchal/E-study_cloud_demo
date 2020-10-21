"""django_circle URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Webapp Urls
    path("", include("app_modules.web_apps.urls")),
    # Django Admin
    path("admin/", admin.site.urls),
    # Django allauth
    path("accounts/", include("allauth.urls")),
    # API Urls
    path("api/v1/", include("app_modules.apis.urls")),
]
