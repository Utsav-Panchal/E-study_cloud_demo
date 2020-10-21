# -*- coding: utf-8 -*-

from django.urls import include, path

from . import views

from .users import urls as users_url

# -----------------------------------------------------------------------------

app_name = "webapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("users/", include(users_url, namespace="users")),
]

# -----------------------------------------------------------------------------
