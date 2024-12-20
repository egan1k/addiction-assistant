from django.contrib import admin
from . import models

@admin.register(models.DashboardLoginLogs)
class DashboardLoginLogsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "when")

    readonly_fields = (
        "email",
        "ip_address",
        "location",
        "is_login_success",
        "errors",
        "when",
    )

    def when(self, obj):
        return obj.created.strftime("%m/%d/%Y %I:%M %p")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False