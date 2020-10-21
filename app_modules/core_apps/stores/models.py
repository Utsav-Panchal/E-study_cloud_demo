import uuid

from app_modules.core_apps.base.models import BaseModel

from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    ImageField,
    IntegerField,
    TextField,
    UUIDField,
)
from django.utils.translation import ugettext_lazy as _


class Store(BaseModel):

    uid = UUIDField(_("UID"), editable=False, default=uuid.uuid4)
    name = CharField(_("Store Name"), blank=False, null=False, max_length=255)
    website = CharField(_("Website"), blank=True, null=True, max_length=255)
    logo = ImageField(_("Logo"), upload_to="uploads/stores/logo", blank=True)
    is_active = BooleanField(_("Active"), default=False)

    def __str__(self):
        return self.name
