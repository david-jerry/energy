from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from etopoenergy.users.forms import UserAdminChangeForm, UserAdminCreationForm
from .models import Kin, JobRequirement, JobRole

User = get_user_model()

admin.site.register(Kin)
admin.site.register(JobRequirement)
admin.site.register(JobRole)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("user_type", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "name", "last_name", "dp", "gender", "email", "phone", "country", "dob", "address", "bvn")}),
        (
            _("Employment Status"),
            {
                "fields": (
                    "status",
                    "role",
                    "certified",
                    "executive",
                    "employed",
                    "unemployed",
                ),
            },
        ),
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
        (
            _("Social"),
            {
                "fields": (
                    "linkedin",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "gender", "first_name", "name", "last_name", "email", "phone", "dob", "address", "bvn", "status", "user_type", "consent", "certified", "executive", "employed", "unemployed", "is_active", "is_superuser"]
    search_fields = ["first_name", "name", "last_name", "email", "phone", "user_type", "bvn"]
    list_filter = ["is_active", 'status', 'consent', "gender"]
    list_editable = ["first_name", "name", "last_name", "is_active", "status", "consent", "user_type", "certified", "executive", "employed", "unemployed"]
