from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from rest_framework.authtoken.models import Token
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "phone_number", "password", "password2")

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return data

    def create(self, validated_data):
        username = validated_data["username"]
        phone_number = validated_data["phone_number"]
        user = User.objects.create_user(phone_number)
        user.username = username
        user.set_password(validated_data["password"])
        user.save()

        token = Token.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            # token = Token.objects.get(user=user)
            # return token
            data["user"] = user
            return data
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."}
        )
