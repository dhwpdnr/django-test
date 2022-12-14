from rest_framework import generics
from .models import User
from .serializers import SignupSerializer, LoginSerializer
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Signup API
class SignupAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        # 세션에 저장(임시)
        request.session["email"] = user.email

        return Response({"Token": token.key}, status=status.HTTP_200_OK)
