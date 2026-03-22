from django.contrib import admin
from django.urls import path, include
from django.utils.html import format_html
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.generic import TemplateView
import os

# Health check endpoint for Railway
def health_check(request):
    return JsonResponse({"status": "healthy", "service": "oda-website"})

# API status endpoint
def api_status(request):
    return JsonResponse({
        "status": "online",
        "version": "1.0.0",
        "service": "oda-website-api"
    })

# لاحظ: حذفنا المسافات والتعليقات الزائدة في الأعلى لتجنب الخطأ
# ولاحظ أن المسار أصبح يبدأ بـ /static/ مباشرة

admin.site.site_header = format_html('<img src="../frontend/public/Website.png" style="height: 30px; vertical-align: middle;"> {}', 'لوحة التحكم موقع oda')
admin.site.site_title = "بوابة الإدارة"
admin.site.index_title = "مرحباً بك في الإدارة"
admin.site.enable_nav_sidebar = False

try:
    admin.site.disable_action('delete_selected')
except KeyError:
    pass

urlpatterns = [
    # Health check endpoint (required for Railway)
    path('health/', health_check, name='health-check'),
    # API status
    path('api/status/', api_status, name='api-status'),
    # Django admin (hidden behind custom path)
    path('oda-secret-access/', admin.site.urls, name='admin-secret-access'),
    # Public API endpoints (versioned)
    path('api/v1/accounts/', include('accounts.api.urls')),
    path('api/v1/stories/', include('stories.api.urls')),
    # Serve frontend index.html for root path
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)