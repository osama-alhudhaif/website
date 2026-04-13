from django.urls import path
from .views import (
    RegistrationAPIView,
    LoginAPIView,
    ProfileAPIView,
    SubscriptionListCreateAPIView,
    SubscriptionDetailAPIView,
    CurrentSubscriptionAPIView,
    SubscriptionPricingAPIView,
    ToggleDarkModeAPIView,
    FollowListCreateAPIView,
    UnfollowAPIView,
    FollowersListAPIView,
    FollowingListAPIView,
    PublicAuthorProfileAPIView,
    VerifyEmailAPIView,
    PasswordResetRequestAPIView,
    PasswordResetConfirmAPIView,
    ChangePasswordAPIView,
)

# هذا الاسم يستخدم للتحويل بين الروابط داخل Django
app_name = 'accounts_api'

urlpatterns = [
    # --- مسارات المصادقة (Authentication) ---
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('me/', ProfileAPIView.as_view(), name='me'),

    # --- التحقق من الإيميل ---
    path('verify-email/<str:uid>/<str:token>/', VerifyEmailAPIView.as_view(), name='verify-email'),

    # --- استعادة كلمة المرور ---
    path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password-reset'),
    path('password-reset/confirm/<str:uid>/<str:token>/', PasswordResetConfirmAPIView.as_view(), name='password-reset-confirm'),

    # --- تغيير كلمة المرور (للمسجلين) ---
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),

    # --- مسارات الاشتراكات (Subscriptions) ---
    path('subscriptions/', SubscriptionListCreateAPIView.as_view(), name='subscription-list'),
    path('subscriptions/<int:pk>/', SubscriptionDetailAPIView.as_view(), name='subscription-detail'),
    path('subscriptions/current/', CurrentSubscriptionAPIView.as_view(), name='current-subscription'),
    path('subscriptions/pricing/', SubscriptionPricingAPIView.as_view(), name='subscription-pricing'),

    # --- الوضع الليلي (Dark Mode) ---
    path('toggle-dark-mode/', ToggleDarkModeAPIView.as_view(), name='toggle-dark-mode'),

    # --- نظام المتابعة (Follows) ---
    path('follows/', FollowListCreateAPIView.as_view(), name='follow-list'),
    path('unfollow/<int:user_id>/', UnfollowAPIView.as_view(), name='unfollow'),
    path('users/<int:user_id>/followers/', FollowersListAPIView.as_view(), name='followers-list'),
    path('users/<int:user_id>/following/', FollowingListAPIView.as_view(), name='following-list'),

    # --- بروفايل المؤلف (Author Profile - يتطلب اشتراك) ---
    path('authors/<int:user_id>/', PublicAuthorProfileAPIView.as_view(), name='author-profile'),
]