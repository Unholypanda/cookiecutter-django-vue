from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('is_active', )

    fieldsets = UserAdmin.fieldsets + (

    )