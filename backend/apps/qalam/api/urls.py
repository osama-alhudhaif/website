from django.urls import path

from .views import QalamChatAPIView


app_name = "qalam_api"

urlpatterns = [
    path("chat/", QalamChatAPIView.as_view(), name="chat"),
]

