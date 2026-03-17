from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, ProfileAPIView


app_name = 'accounts_api'

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('me/', ProfileAPIView.as_view(), name='me'),
]

