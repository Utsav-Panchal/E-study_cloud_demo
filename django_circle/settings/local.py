from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="BQY2FNNDk16DdZd4y8mf6n36HV2y22SszOxMQ3yGDzh9TlvYQmFEYeurc1UEJKBz",
)

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default="Django Circle <noreply@djangocircle.com>"
)
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Django Circle]")

