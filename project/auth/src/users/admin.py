from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'role', )
    readonly_fields = ('public_id', 'pk',)
    fieldsets = (
        ('General', {
            'fields': ('username', 'password', 'role', )
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', )
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', )
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'role', )
        }),
    )