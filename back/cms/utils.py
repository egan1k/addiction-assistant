from django.contrib.auth import authenticate

from .models import DashboardLoginLogs


def log_dashboard_login(email, ip_address, is_success, error_message=None):
    """
    logging try to entry dashboard.

    Args:
        email (str): user email.
        ip_address (str): IP-address client.
        is_success (bool): success entry.
        error_message (str, optional): message success or failure. Defaults to None.
    """
    log = DashboardLoginLogs.objects.create(
        email=email, ip_address=ip_address, is_login_success=is_success
    )
    if not is_success and error_message:
        log.errors = error_message
        log.save()


def authenticate_user(email, password, request):
    user = authenticate(request=request, email=email, password=password)
    return user


def is_user_credentials_are_valid(email, password, request):
    user = authenticate_user(email, password, request)
    if user:
        return True
    return False