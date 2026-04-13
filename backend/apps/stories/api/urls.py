from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    StoryViewSet, CommentListCreateAPIView, CommentDetailAPIView,
    RatingListCreateAPIView, UserRatingAPIView
)
from .translation import TranslateTextAPIView, SupportedLanguagesAPIView


app_name = 'stories_api'

router = DefaultRouter()
router.register('stories', StoryViewSet, basename='story')

urlpatterns = [
    path('', include(router.urls)),

    # Comments
    path('stories/<int:story_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),

    # Ratings
    path('stories/<int:story_id>/ratings/', RatingListCreateAPIView.as_view(), name='rating-list'),
    path('stories/<int:story_id>/my-rating/', UserRatingAPIView.as_view(), name='user-rating'),

    # Translation
    path('translate/', TranslateTextAPIView.as_view(), name='translate'),
    path('translate/languages/', SupportedLanguagesAPIView.as_view(), name='supported-languages'),
]

