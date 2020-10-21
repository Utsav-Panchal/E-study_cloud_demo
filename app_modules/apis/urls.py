from django.conf import settings
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

schema_view = get_schema_view(
    openapi.Info(title=settings.PROJECT_TITLE, default_version="v1",),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


app_name = "api"
urlpatterns = [
    path("rest-auth/", include("app_modules.apis.auth.urls"), name="authentication",),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
