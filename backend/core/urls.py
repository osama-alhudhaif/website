from django.contrib import admin
from django.urls import path, include
from django.utils.html import format_html
from django.conf import settings
from django.conf.urls.static import static

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
    # Django admin (hidden behind custom path)
    path('oda-secret-access/', admin.site.urls, name='admin-secret-access'),
    # Public API endpoints (versioned)
    path('api/v1/accounts/', include('accounts.api.urls')),
    path('api/v1/stories/', include('stories.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)