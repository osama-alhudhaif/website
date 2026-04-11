from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.html import format_html
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.static import serve
from core.views import fixed_serve
import os

def health_check(request):
    return JsonResponse({"status": "healthy", "service": "oda-website"})

def api_status(request):
    return JsonResponse({"status": "online", "version": "1.0.0", "service": "oda-website-api"})

admin.site.site_header = format_html('<img src="/static/assets/Website-DOofmHeX.png" style="height: 30px; vertical-align: middle;"> {}', 'لوحة التحكم موقع أودا')
admin.site.site_title = "بوابة الإدارة"
admin.site.index_title = "مرحباً بك في الإدارة"
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('health/', health_check, name='health-check'),
    path('api/status/', api_status, name='api-status'),
    path('oda-secret-access/', admin.site.urls, name='admin-secret-access'),
    path('api/v1/accounts/', include('accounts.api.urls')),
    path('api/v1/stories/', include('stories.api.urls')),
    
    # 1. Serve Vite assets directly with fixed serve view
    re_path(r'^assets/(?P<path>.*)$', fixed_serve, {
        'document_root': str(os.path.join(settings.BASE_DIR, 'frontend/dist/assets')),
    }),
    
    # 2. Serve other static files directly with fixed serve view
    re_path(r'^static/(?P<path>.*)$', fixed_serve, {
        'document_root': str(os.path.join(settings.BASE_DIR, 'frontend/dist')),
    }),
    
    # 2. الصفحة الرئيسية
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    
    # 3. أي مسار آخر يوجه لـ index.html (لحماية React Router)
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)