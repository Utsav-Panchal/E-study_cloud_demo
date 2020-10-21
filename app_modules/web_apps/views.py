from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


class IndexView(TemplateView):
    template_name = "webapp/index.html"

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect(reverse("account_login"))

        return super().dispatch(request, *args, **kwargs)
