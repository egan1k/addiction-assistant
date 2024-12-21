from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.utils import get_client_ipv4
from cms.utils import is_user_credentials_are_valid, log_dashboard_login, authenticate_user


class AuthorizationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        ip_address = get_client_ipv4(request)

        if not is_user_credentials_are_valid(email, password, request):
            log_dashboard_login(
                email, ip_address, False, error_message="Wrong credentials"
            )
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate_user(email, password, request)
        have_access = True
        status_code = status.HTTP_200_OK if have_access else status.HTTP_400_BAD_REQUEST
        response_data = {"have access": have_access}
        error_message = None
        is_success = have_access

        if not have_access:
            response_data["error"] = "You don't have permissions to access the Dashboard"
            error_message = "Don't have permissions to access the Dashboard"
            is_success = False

        Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)
        response_data["access"] = token.key
        log_dashboard_login(email, ip_address, is_success, error_message=error_message)
        return Response(response_data, status=status_code)