from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.html import format_html
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.generic import TemplateView
from core.views import fixed_serve
import os


def health_check(request):
    return JsonResponse({"status": "healthy", "service": "oda-website"})


def api_status(request):
    return JsonResponse({"status": "online", "version": "1.0.0", "service": "oda-website-api"})


admin.site.site_header = format_html(
    '<img src="/static/assets/Website-DOofmHeX.png" style="height: 30px; vertical-align: middle;"> {}',
    'لوحة التحكم موقع أودا'
)
admin.site.site_title = "بوابة الإدارة"
admin.site.index_title = "مرحباً بك في الإدارة"
admin.site.enable_nav_sidebar = False


# مسارات الـ API الأساسية (دائماً متاحة)
urlpatterns = [
    # صفحات النظام
    path('health/', health_check, name='health-check'),
    path('api/status/', api_status, name='api-status'),
    path('oda-secret-access/', admin.site.urls, name='admin-secret-access'),
    # صفحات المستخدمين
    path('api/v1/accounts/', include('accounts.api.urls')),
    # صفحات القصص
    path('api/v1/stories/', include('stories.api.urls')),

    # ملفات الوسائط المرفوعة (دائماً متاحة)
    re_path(r'^media/(?P<path>.*)$', fixed_serve, {
        'document_root': str(settings.MEDIA_ROOT),
    }),
]

# مسارات الـ Frontend — تُضاف فقط لو الـ build موجود
FRONTEND_DIST = os.path.join(settings.BASE_DIR, 'frontend', 'dist')
FRONTEND_BUILT = os.path.exists(os.path.join(FRONTEND_DIST, 'index.html'))

if FRONTEND_BUILT:
    urlpatterns += [
        re_path(r'^assets/(?P<path>.*)$', fixed_serve, {
            'document_root': os.path.join(FRONTEND_DIST, 'assets'),
        }),
        re_path(r'^static/(?P<path>.*)$', fixed_serve, {
            'document_root': FRONTEND_DIST,
        }),
        path('', TemplateView.as_view(template_name='index.html'), name='index'),
        # React Router fallback — يستبعد مسارات الـ backend
        re_path(
            r'^(?!api/|oda-secret-access/|media/|health/|assets/|static/).*$',
            TemplateView.as_view(template_name='index.html'),
        ),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)