# -*- coding: utf-8 -*-

from django.urls import path
from rest_auth.registration.views import VerifyEmailView
from rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
    UserDetailsView,
)
from rest_auth.registration.views import RegisterView
from rest_framework.decorators import authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


app_name = "auth"

urlpatterns = [
    path("login/", authentication_classes([])(LoginView).as_view(), name="user_login"),
    path(
        "registration/",
        authentication_classes([])(RegisterView).as_view(),
        name="user_signup",
    ),
    path(
        "registration/verify-email/",
        VerifyEmailView.as_view(),
        name="user_verify_email",
    ),
    path("password/reset/", PasswordResetView.as_view(), name="user_password_reset"),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="user_password_reset_confirm",
    ),
    path(
        "password/change/",
        authentication_classes([JSONWebTokenAuthentication])(
            PasswordChangeView
        ).as_view(),
        name="rest_password_change",
    ),
    path(
        "logout/", authentication_classes([])(LogoutView).as_view(), name="user_logout"
    ),
    path(
        "user/",
        authentication_classes([JSONWebTokenAuthentication])(UserDetailsView).as_view(),
        name="rest_user_details",
    ),
]
