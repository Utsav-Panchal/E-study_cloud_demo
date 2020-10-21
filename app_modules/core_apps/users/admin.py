from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ["username", "email", "first_name", "is_superuser"]
    search_fields = ["username", "email"]
