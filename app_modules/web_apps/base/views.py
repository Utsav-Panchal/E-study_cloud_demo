from django.contrib import messages
from django.contrib.auth import get_permission_codename
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.utils.translation import gettext as _
from django.utils.translation import ngettext
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
from django.contrib.admin.utils import NestedObjects
from django.views.generic.edit import FormView
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.text import capfirst


from .mixins import HasPermissionsMixin, ModelOptsMixin, SuccessMessageMixin
from app_modules.utils import app_urlname

MSG_CREATED = '"{}" created successfully.'
MSG_UPDATED = '"{}" updated successfully.'
MSG_DELETED = '"{}" deleted successfully.'
MSG_CANCELED = '"{}" canceled successfully.'

# -----------------------------------------------------------------------------
# Generic Views
# -----------------------------------------------------------------------------


class BaseView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """View with LoginRequiredMixin and PermissionRequiredMixin."""

    def get_success(self, message):
        response_data = {}
        response_data["result"] = True
        response_data["message"] = message
        return JsonResponse(response_data)

    def get_error(self, message, status_code=400):
        response_data = {}
        response_data["result"] = False
        response_data["message"] = message
        return JsonResponse(response_data, status=status_code)


class BaseLoginRequiredView(LoginRequiredMixin, View):
    """View with LoginRequiredMixin."""

    pass


class BaseTemplateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    """TemplateView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    """FormView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    ListView,
):
    """ListView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, ModelOptsMixin, DetailView
):
    """DetailView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    CreateView,
):
    """CreateView CBV with LoginRequiredMixin, PermissionRequiredMixin
    and SuccessMessageMixin."""

    def get_success_message(self):
        return MSG_CREATED.format(self.object)

    def get_success_url(self):

        opts = self.model._meta
        return reverse(app_urlname(opts, "list", self.request.user))


class BaseUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    UpdateView,
):
    """UpdateView CBV with LoginRequiredMixin, PermissionRequiredMixin
    and SuccessMessageMixin."""

    def get_permission_required(self):
        """Default to view and change perms."""
        required_perms = super().get_permission_required()

        opts = self.model._meta
        codename_view = get_permission_codename("view", opts)
        codename_change = get_permission_codename("change", opts)
        view_perm = f"{opts.app_label}.{codename_view}"
        change_perm = f"{opts.app_label}.{codename_change}"
        perms = (view_perm, change_perm)

        return set(required_perms + perms)

    def get_success_message(self):
        return MSG_UPDATED.format(self.object)

    def get_success_url(self):

        opts = self.model._meta
        return reverse(app_urlname(opts, "list", self.request.user))


class BaseDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    DeleteView,
):
    """CBV to delete a model record - both Ajax and POST requests."""

    def get_success_message(self):
        return MSG_DELETED.format(self.object)

    def get_success_url(self):
        opts = self.model._meta
        return reverse(app_urlname(opts, "list", self.request.user))

    def delete(self, request, *args, **kwargs):
        """Override delete method."""
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.get_success_message())
        if self.request.is_ajax():
            response_data = {}
            response_data["result"] = True
            response_data["message"] = self.get_success_message()
            return JsonResponse(response_data)
        return response

    def get_context_data(self, **kwargs):
        """Get deletable objects."""
        ctx = super().get_context_data(**kwargs)

        opts = self.model._meta

        # Populate deleted_objects, a data structure of all related objects that
        # will also be deleted.
        # deleted_objects, model_count, perms_needed, protected = self.get_deleted_objects([obj], request)
        deleted_objects, model_count, protected = self.get_deleted_objects(
            [self.object]
        )

        object_name = str(opts.verbose_name)

        # if perms_needed or protected:
        if protected:
            title = _("Cannot delete %(name)s") % {"name": object_name}
        else:
            title = _("Are you sure?")

        ctx["title"] = title
        ctx["deleted_objects"] = deleted_objects
        ctx["model_count"] = dict(model_count).items()
        ctx["protected"] = protected
        return ctx

    @staticmethod
    def get_deleted_objects(objs):
        """Based on `django/contrib/admin/utils.py`"""
        collector = NestedObjects(using="default")
        collector.collect(objs)

        def format_callback(obj):
            opts = obj._meta
            # Display a link to the admin page.
            try:
                return format_html(
                    '{}: <a href="{}">{}</a>',
                    capfirst(opts.verbose_name),
                    reverse(app_urlname(opts, "update"), kwargs={"pk": obj.pk}),
                    obj,
                )
            except NoReverseMatch:
                pass

            no_edit_link = "%s: %s" % (capfirst(opts.verbose_name), force_text(obj))
            return no_edit_link

        to_delete = collector.nested(format_callback)
        protected = [format_callback(obj) for obj in collector.protected]
        model_count = {
            model._meta.verbose_name_plural: len(objs)
            for model, objs in collector.model_objs.items()
        }

        return to_delete, model_count, protected
