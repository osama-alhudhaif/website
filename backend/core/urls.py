"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path
from django.utils.html import format_html

# لاحظ: حذفنا المسافات والتعليقات الزائدة في الأعلى لتجنب الخطأ
# ولاحظ أن المسار أصبح يبدأ بـ /static/ مباشرة

admin.site.site_header = format_html('<img src="/static/Website.png" style="height: 30px; vertical-align: middle;"> لوحة التحكم موقع oda')
admin.site.site_title = "بوابة الإدارة"
admin.site.index_title = "مرحباً بك في الإدارة"
admin.site.enable_nav_sidebar = False

try:
    admin.site.disable_action('delete_selected')
except KeyError:
    pass

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('oda-secret-access/', admin.site.urls, name='admin-secret-access'),
]