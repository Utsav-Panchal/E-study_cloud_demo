from django import forms

from app_modules.core_apps.users.models import User


class UserProfileForm(forms.ModelForm):
    """
    Form to update user profile details
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
