from django.urls import path

from .views import (
    RegistrationAPIView, LoginAPIView, ProfileAPIView,
    SubscriptionListCreateAPIView, SubscriptionDetailAPIView,
    CurrentSubscriptionAPIView, SubscriptionPricingAPIView,
    ToggleDarkModeAPIView, FollowListCreateAPIView, UnfollowAPIView,
    FollowersListAPIView, FollowingListAPIView, PublicAuthorProfileAPIView
)


app_name = 'accounts_api'

urlpatterns = [
    # Auth
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('me/', ProfileAPIView.as_view(), name='me'),

    # Subscriptions
    path('subscriptions/', SubscriptionListCreateAPIView.as_view(), name='subscription-list'),
    path('subscriptions/<int:pk>/', SubscriptionDetailAPIView.as_view(), name='subscription-detail'),
    path('subscriptions/current/', CurrentSubscriptionAPIView.as_view(), name='current-subscription'),
    path('subscriptions/pricing/', SubscriptionPricingAPIView.as_view(), name='subscription-pricing'),

    # Dark Mode
    path('toggle-dark-mode/', ToggleDarkModeAPIView.as_view(), name='toggle-dark-mode'),

    # Follows
    path('follows/', FollowListCreateAPIView.as_view(), name='follow-list'),
    path('unfollow/<int:user_id>/', UnfollowAPIView.as_view(), name='unfollow'),
    path('users/<int:user_id>/followers/', FollowersListAPIView.as_view(), name='followers-list'),
    path('users/<int:user_id>/following/', FollowingListAPIView.as_view(), name='following-list'),

    # Author Profile (requires subscription)
    path('authors/<int:user_id>/', PublicAuthorProfileAPIView.as_view(), name='author-profile'),
]

