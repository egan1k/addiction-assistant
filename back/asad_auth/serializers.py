from django.contrib.auth import authenticate
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from main.models import User
from main.utils import block_user, get_client_ipv4
from main.constants import DASHBOARD_ONLY_ACCESS_ACCOUNT_TYPES

import cms.utils


class CustomTokenSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        username = attrs.get("username") or attrs.get("email")
        password = attrs.get("password")
        request = self.context.get("request")
        ip_address = get_client_ipv4(request)

        if username and password:
            user = authenticate(
                request=request, username=username.lower(), password=password
            )
            error_log_message = None

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)

            if not user:
                try:
                    user_instance = User.objects.get(email=username)
                    if user_instance.account_type in DASHBOARD_ONLY_ACCESS_ACCOUNT_TYPES:
                        cms.utils.log_dashboard_login(
                            user_instance.email,
                            ip_address,
                            False,
                            error_message="Wrong credentials",
                        )
                except Exception:
                    msg = _("No active account found with the given credentials.")
                    raise serializers.ValidationError(msg, code="authorization")

                is_dashboard_user = (
                    user_instance.account_type in DASHBOARD_ONLY_ACCESS_ACCOUNT_TYPES
                )
                if user_instance.is_locked:
                    msg = _(
                        "Your account is locked."
                        " Contact your ASAD administrator or support."
                    )
                    error_log_message = "Locked account."
                    if is_dashboard_user:
                        cms.utils.log_dashboard_login(
                            user.email,
                            ip_address,
                            False,
                            error_message=error_log_message,
                        )
                    raise serializers.ValidationError(msg, code="authorization")
                user_instance.login_attempts_left -= 1
                user_instance.last_failed_login_attempt = timezone.now()
                user_instance.save(
                    update_fields=["login_attempts_left", "last_failed_login_attempt"]
                )
                attempts_left = user_instance.login_attempts_left
                msg = _("No active account found with the given credentials.")
                if attempts_left == 0:
                    block_user(user_instance)
                    msg = _(
                        "Your account is locked."
                        " Contact your ASAD administrator or support."
                    )
                    error_log_message = "Locked account."
                    if is_dashboard_user:
                        cms.utils.log_dashboard_login(
                            user.email,
                            ip_address,
                            False,
                            error_message=error_log_message,
                        )
                    raise serializers.ValidationError(msg, code="authorization")
                data = {"non_field_errors": msg, "attempts_left": [attempts_left]}
                raise serializers.ValidationError(data)
            elif user.is_locked:
                msg = _(
                    "Your account is locked."
                    " Contact your ASAD administrator or support."
                )
                error_log_message = "Locked account."
                if user.account_type in DASHBOARD_ONLY_ACCESS_ACCOUNT_TYPES:
                    cms.utils.log_dashboard_login(
                        user.email, ip_address, False, error_message=error_log_message
                    )
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        user.last_login = timezone.now()
        user.save(update_fields=["last_login"])
        if user.account_type in DASHBOARD_ONLY_ACCESS_ACCOUNT_TYPES:
            cms.utils.log_dashboard_login(user.email, ip_address, True)
        attrs["user"] = user
        return attrs
