from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from etopoenergy.users.forms import UserAdminChangeForm, UserAdminCreationForm
from .models import Kin

User = get_user_model()

admin.site.register(Kin)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "gender", "email", "phone", "dob", "address", "bvn")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "consent",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "gender", "name", "email", "phone", "dob", "address", "bvn", "status", "user_type", "consent", "is_active", "is_superuser"]
    search_fields = ["name", "email", "phone", "user_type", "bvn"]
    list_filter = ["is_active", 'status', 'consent', "gender"]
    list_editable = ["is_active", "status", "consent", "user_type"]
