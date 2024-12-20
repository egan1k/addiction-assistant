from django.db import models
from model_utils.models import TimeStampedModel


class DashboardLoginLogs(TimeStampedModel):
    email = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.CharField("IP Address", max_length=20)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_login_success = models.BooleanField("Success", default=False)
    errors = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.is_login_success:
            return f"{self.email} successfully logged into the dashboard"
        return f"{self.email} tried to log into the dashboard"

    class Meta:
        verbose_name = "Dashboard Login Log"
        verbose_name_plural = "Dashboard Login Logs"
