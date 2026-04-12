from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","first_name","last_name","role","phone","country","gender","date_of_birth","dark_mode_enabled","date_joined"]
        read_only_fields = ["id", "date_joined"]


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2", "role"]

    def validate(self, attrs):
        if attrs["password"] != attrs.pop("password2"):
            raise serializers.ValidationError({"password": "كلمتا المرور غير متطابقتين"})
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
