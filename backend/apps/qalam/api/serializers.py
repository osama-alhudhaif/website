from rest_framework import serializers

from qalam.models import QalamSession, QalamMessage


class QalamMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = QalamMessage
        fields = ["id", "role", "content", "created_at"]
        read_only_fields = ["id", "created_at"]


class QalamSessionSerializer(serializers.ModelSerializer):
    messages = QalamMessageSerializer(many=True, read_only=True)

    class Meta:
        model = QalamSession
        fields = ["id", "mode", "story", "created_at", "updated_at", "messages"]
        read_only_fields = ["id", "created_at", "updated_at", "messages"]


class QalamChatRequestSerializer(serializers.Serializer):
    session_id = serializers.IntegerField(required=False)
    message = serializers.CharField()
    mode = serializers.ChoiceField(
        choices=[choice[0] for choice in QalamSession.MODE_CHOICES],
        required=False,
    )
    story_id = serializers.IntegerField(required=False)

