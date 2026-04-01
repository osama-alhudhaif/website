from django.urls import path
# الاستيراد من ملف views.py الموجود في نفس مجلد api
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
    PublicAuthorProfileAPIView
)

# هذا الاسم يستخدم للتحويل بين الروابط داخل Django
app_name = 'accounts_api'

urlpatterns = [
    # --- مسارات المصادقة (Authentication) ---
    # الرابط الكامل: /api/v1/accounts/register/
    path('register/', RegistrationAPIView.as_view(), name='register'),
    
    # الرابط الكامل: /api/v1/accounts/login/
    path('login/', LoginAPIView.as_view(), name='login'),
    
    # الرابط الكامل: /api/v1/accounts/me/ (للملف الشخصي الحالي)
    path('me/', ProfileAPIView.as_view(), name='me'),

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