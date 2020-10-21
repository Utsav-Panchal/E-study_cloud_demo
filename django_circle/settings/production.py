from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = False
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="BQY2FNNDk16DdZd4y8mf6n36HV2y22SszOxMQ3yGDzh9TlvYQmFEYeurc1UEJKBz",
)
