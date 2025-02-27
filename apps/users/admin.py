from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'avatar', 'is_instructor')}),
    )
    list_display = ['username', 'email', 'is_instructor']
    search_fields = ['username', 'email']
