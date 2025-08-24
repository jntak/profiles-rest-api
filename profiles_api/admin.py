from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class UserProfileAdmin(UserAdmin):
    """Define admin pages for users"""

    ordering = ["id"]
    list_display = ["email", "name", "is_staff", "is_superuser"]

    # What fields appear when editing/adding users
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login",)}),
    )

    # Fields shown when creating a new user via admin
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "password1", "password2", "is_active", "is_staff", "is_superuser"),
            },
        ),
    )

    search_fields = ("email", "name")
    readonly_fields = ("last_login",)


# Register with admin site
admin.site.register(UserProfile, UserProfileAdmin)
