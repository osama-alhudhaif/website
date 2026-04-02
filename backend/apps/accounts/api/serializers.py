from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts.models import User, Subscription, Follow


class UserSerializer(serializers.ModelSerializer):
    has_active_subscription = serializers.SerializerMethodField()
    subscription_info = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name",
            "phone", "country", "role", "gender", "date_of_birth",
            "dark_mode_enabled", "has_active_subscription",
            "subscription_info", "followers_count", "following_count",
        ]
        read_only_fields = ["id"]

    def get_has_active_subscription(self, obj):
        return obj.has_active_subscription()

    def get_subscription_info(self, obj):
        subscription = obj.get_active_subscription()
        if subscription:
            return {
                "plan_type": subscription.plan_type,
                "plan_type_display": subscription.get_plan_type_display(),
                "end_date": subscription.end_date,
                "days_remaining": subscription.days_remaining(),
            }
        return None

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            "username", "email", "first_name", "last_name",
            "password", "password_confirm", "date_of_birth",
            "gender", "country", "role",
        ]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password_confirm"):
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs.get("username"), password=attrs.get("password"))
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        attrs["user"] = user
        return attrs


class SubscriptionSerializer(serializers.ModelSerializer):
    plan_type_display = serializers.CharField(source="get_plan_type_display", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = [
            "id", "plan_type", "plan_type_display", "status", "status_display",
            "is_active", "monthly_price", "yearly_price", "educational_price",
            "price", "start_date", "end_date", "days_remaining", "auto_renew", "created_at",
        ]
        read_only_fields = ["id", "status", "is_active", "start_date", "end_date", "days_remaining", "created_at"]

    def get_price(self, obj):
        return obj.get_price()


class FollowSerializer(serializers.ModelSerializer):
    follower_username = serializers.CharField(source="follower.username", read_only=True)
    following_username = serializers.CharField(source="following.username", read_only=True)

    class Meta:
        model = Follow
        fields = ["id", "follower", "follower_username", "following", "following_username", "created_at"]
        read_only_fields = ["id", "created_at"]