from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import StoryViewSet # ????: ??? ?????? ??? ??????

# router = DefaultRouter()
# router.register(r'stories', StoryViewSet, basename='story')

urlpatterns = [
    # path('register/', RegistrationAPIView.as_view(), name='register'),
    # path('login/', LoginAPIView.as_view(), name='login'),
]

# urlpatterns += router.urls
