from rest_framework import serializers
from .models import UserAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            "id",
            "parameters",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_image",
            "email_confirmed",
        )
        read_only_fields = ("username",)


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = UserAccount.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserAccount
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_image",
            "email_confirmed",
        )
        extra_kwargs = {"password": {"write_only": True}}
