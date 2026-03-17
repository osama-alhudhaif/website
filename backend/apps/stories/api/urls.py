from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StoryViewSet


app_name = 'stories_api'

router = DefaultRouter()
router.register('stories', StoryViewSet, basename='story')

urlpatterns = [
    path('', include(router.urls)),
]

