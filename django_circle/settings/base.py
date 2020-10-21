"""
Base settings to build other settings files upon.
"""
import datetime
import os
from pathlib import Path
from typing import Dict, Union

import environ
from django.contrib.messages import constants as messages

env = environ.Env()

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

project_title = env.str("PROJECT_TITLE", "Django Circle").lower().replace(" ", "_")

APPS_DIR = ROOT_DIR / "app_modules"

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
TIME_ZONE = "US/Eastern"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
if os.getenv("GAE_APPLICATION"):
    DATABASE_HOST = "/cloudsql/{}".format(env("CSQL_CONNECTION_NAME"))
else:
    DATABASE_HOST = "127.0.0.1"

DATABASES: Dict[str, Dict[str, Union[str, int]]] = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": DATABASE_HOST,
        "NAME": env.str("DATABASE_NAME", project_title),
        "USER": env.str("DATABASE_USER", ""),
        "PASSWORD": env.str("DATABASE_PASSWORD", ""),
        "CONN_MAX_AGE": 500,
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = "django_circle.urls"

WSGI_APPLICATION = "django_circle.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
    "django.contrib.humanize",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # "allauth.socialaccount.providers.facebook",
    # "allauth.socialaccount.providers.google",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_yasg",  # Swagger Documentation
    "rest_auth",
]

LOCAL_APPS = [
    "django_circle",
    "app_modules.web_apps.apps.WebAppConfig",
    "app_modules.core_apps.users.apps.UsersConfig",
    "app_modules.core_apps.stores.apps.StoresConfig"
    # Your stuff: custom apps go here
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "webapp:index"
LOGIN_URL = "account_login"
ACCOUNT_LOGOUT_ON_GET = True


# PASSWORDS
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
STATIC_ROOT = str(APPS_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(ROOT_DIR / "media")
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "templates")],
        # "APP_DIRS": True,
        "OPTIONS": {
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

CRISPY_TEMPLATE_PACK = "bootstrap4"

# FIXTURES
# ------------------------------------------------------------------------------
FIXTURE_DIRS = (
    str(APPS_DIR / "fixtures"),
    os.path.join(ROOT_DIR, project_title, "api", "fixtures"),
)

# SECURITY
# ------------------------------------------------------------------------------
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
ADMINS = [(env("ADMIN_NAME"), env("ADMIN_EMAIL"))]
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE

CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 60
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

CELERY_RESULT_BACKEND = "django-db"
# CELERY_RESULT_BACKEND = env("CELERY_BROKER_URL")
CELERY_SEND_TASK_SENT_EVENT = True

CELERY_IMPORTS = ()

# Other Celery settings
# CELERY_BEAT_SCHEDULE = {
#     'reset-leaderboard': {
#         'task': 'leaderboard_task',
#         'schedule': crontab(minute=1),
#     },
# }


# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_ADAPTER = ""
# ACCOUNT_FORMS = {
#     # "signup": "",
# }
# SOCIALACCOUNT_ADAPTER = ""
# SOCIALACCOUNT_AUTO_SIGNUP = False
# SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
# SOCIALACCOUNT_FORMS = {"signup": ""}

SOCIALACCOUNT_PROVIDERS = {
    "facebook": {
        "METHOD": "oauth2",
        "SDK_URL": "//connect.facebook.net/{locale}/sdk.js",
        "SCOPE": ["email", "public_profile"],
        "AUTH_PARAMS": {"auth_type": "reauthenticate"},
        "INIT_PARAMS": {"cookie": True},
        "FIELDS": [
            "id",
            "email",
            "name",
            "first_name",
            "last_name",
            "verified",
            "locale",
            "timezone",
            "link",
            "gender",
            "updated_time",
        ],
        "EXCHANGE_TOKEN": True,
        # 'LOCALE_FUNC': 'path.to.callable',
        "VERIFIED_EMAIL": False,
        "VERSION": "v7.0",
    },
    "google": {
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "offline"},
    },
}

# django-rest-framework
# -------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DATETIME_FORMAT": "iso-8601",  # "%Y-%m-%d %H:%M:%S",  # 'iso-8601'
    "DATE_FORMAT": "%Y-%m-%d",
    "TIME_FORMAT": "%H:%M:%S",
    "DATETIME_INPUT_FORMATS": ["%Y-%m-%d %H:%M:%S"],
    "DEFAULT_RENDERER_CLASSES": ["app_modules.apis.base.renderers.BaseAPIJSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

REST_USE_JWT = True

JWT_AUTH = {
    "JWT_ENCODE_HANDLER": "rest_framework_jwt.utils.jwt_encode_handler",
    "JWT_DECODE_HANDLER": "rest_framework_jwt.utils.jwt_decode_handler",
    "JWT_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_payload_handler",
    "JWT_PAYLOAD_GET_USER_ID_HANDLER": "rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler",
    "JWT_RESPONSE_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_response_payload_handler",
    "JWT_GET_USER_SECRET_KEY": None,
    "JWT_PUBLIC_KEY": None,
    "JWT_PRIVATE_KEY": None,
    "JWT_ALGORITHM": "HS256",
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LEEWAY": 0,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(hours=24),
    "JWT_AUDIENCE": None,
    "JWT_ISSUER": None,
    "JWT_ALLOW_REFRESH": False,
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=7),
    "JWT_AUTH_HEADER_PREFIX": "JWT",
    "JWT_AUTH_COOKIE": None,
}

# Swagger API Documentation
# -------------------------------------------------------------------------------
SWAGGER_SETTINGS = {
    "DOC_EXPANSION": "list",
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "JWT": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
    "REFETCH_SCHEMA_WITH_AUTH": True,
}

# cors-headers
# ------------------------------------------------------------------------------
CORS_URLS_REGEX = r"^/api/.*$"
CORS_ORIGIN_ALLOW_ALL = True
# custom-admin
# -------------------------------------------------------------------------------
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# Used in customadmin.context_processors.common
PROJECT_TITLE = env("PROJECT_TITLE")
COPYRIGHT = env("PROJECT_TITLE")
