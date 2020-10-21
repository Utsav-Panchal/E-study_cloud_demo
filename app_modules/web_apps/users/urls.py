# -*- coding: utf-8 -*-

from django.urls import include, path

from . import views

app_name = "users"

# This file contains only user related routing urls
urlpatterns = [
    path("settings/", views.UserProfileSettingView.as_view(), name="user-settings"),
]
