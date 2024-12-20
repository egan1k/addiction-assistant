from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from asad_auth.serializers import CustomTokenSerializer


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]


        Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "access": token.key,
                "user_id": user.pk,
                "email": user.email,
            }
        )
