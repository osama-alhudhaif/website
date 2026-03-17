from asgiref.sync import async_to_sync
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from qalam.models import QalamSession, QalamMessage
from qalam.services import call_qalam_chat
from stories.models import Story
from .serializers import (
    QalamSessionSerializer,
    QalamChatRequestSerializer,
)


class QalamChatAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = QalamChatRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        session_id = data.get("session_id")
        mode = data.get("mode") or "chat"
        story_id = data.get("story_id")

        session = None
        if session_id:
            try:
                session = QalamSession.objects.get(id=session_id, user=request.user)
            except QalamSession.DoesNotExist:
                return Response(
                    {"detail": "Session not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

        if session is None:
            story = None
            if story_id:
                story = Story.objects.filter(id=story_id).first()
            session = QalamSession.objects.create(
                user=request.user,
                story=story,
                mode=mode,
            )

        QalamMessage.objects.create(
            session=session,
            role="user",
            content=data["message"],
        )

        history = [
            {"role": m.role, "content": m.content} for m in session.messages.all()
        ]

        assistant_reply = async_to_sync(call_qalam_chat)(
            session_id=session.id,
            messages=history,
            mode=mode,
            metadata={"story_id": story_id},
        )

        QalamMessage.objects.create(
            session=session,
            role="assistant",
            content=assistant_reply,
        )

        response_data = QalamSessionSerializer(session).data
        return Response(response_data, status=status.HTTP_200_OK)

