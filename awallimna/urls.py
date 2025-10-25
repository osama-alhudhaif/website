"""
URL configuration for awallimna project.

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
from django.contrib import admin
from django.urls import path, include  # 1. تم إضافة 'include' هنا

# تم حذف السطر الخاطئ: from . import views

urlpatterns = [
    # 2. مسار لوحة الإدارة (لا يتغير)
    path('admin/', admin.site.urls),
    
    # 3. ربط جميع روابط تطبيق 'stories_app' بالمسار الرئيسي للموقع ('')
    path('', include('stories_app.urls')),
]