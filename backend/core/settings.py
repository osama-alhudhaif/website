"""
Django settings for core project.
Modified for Oda Project - Local AI Privacy focus.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Django 6.0.4 pathlib compatibility fix
from pathlib import PurePosixPath
import re

def patched_validate_file_name(name, allow_relative_path=False):
    """
    Complete replacement for validate_file_name that handles pathlib objects.
    This fixes the Django 6.0.4 'PurePosixPath' object has no attribute 'is_absolute' error.
    """
    # Convert pathlib objects to string
    if hasattr(name, 'as_posix') or isinstance(name, PurePosixPath):
        name = str(name)
    
    # Original Django validation logic (copied from Django source)
    if not name:
        raise ValueError('The provided file name is empty.')
    
    # Simple string-based validation to avoid pathlib issues
    if not allow_relative_path and (name.startswith('/') or (len(name) > 1 and name[1] == ':')):
        raise ValueError('Absolute file paths are not allowed.')
    
    if '..' in name.split('/') or '..' in name.split('\\'):
        raise ValueError('File paths cannot contain ".." components.')
    
    # Check for invalid characters
    if re.search(r'[<>:"|?*]', name):
        raise ValueError('File name contains invalid characters.')
    
    return name

# Apply monkey patch
import django.core.files.utils
django.core.files.utils.validate_file_name = patched_validate_file_name

# Additional fix for get_available_name pathlib issues
from django.core.files.storage import Storage
original_get_available_name = Storage.get_available_name

def patched_get_available_name(self, name, max_length=None):
    """
    Patched version that handles pathlib objects in get_available_name.
    """
    # Convert pathlib objects to string
    if hasattr(name, 'as_posix') or isinstance(name, PurePosixPath):
        name = str(name)
    
    # Call original method with string name
    return original_get_available_name(self, name, max_length)

# Apply the patch
Storage.get_available_name = patched_get_available_name

# Fix Django 6 autoreload pathlib issues
import django.utils.autoreload
from pathlib import Path as OriginalPath

# Monkey patch Path.with_suffix for Django 6 compatibility
def patched_with_suffix(self, suffix):
    """Fixed version of with_suffix that works with Django 6"""
    return str(self).rsplit('.', 1)[0] + suffix

# Apply the monkey patch to fix autoreload
if hasattr(OriginalPath, 'with_suffix'):
    original_with_suffix = OriginalPath.with_suffix
    OriginalPath.with_suffix = patched_with_suffix

BASE_DIR = Path(__file__).resolve().parent.parent

env_path = BASE_DIR / '.env'
if env_path.exists():
    load_dotenv(env_path)
else:
    load_dotenv(BASE_DIR.parent / '.env')

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    if os.getenv('DJANGO_ENV') == 'production':
        raise ValueError("SECRET_KEY must be set in production!")
    SECRET_KEY = 'django-insecure-dev-only-key-change-in-production'

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'whitenoise.runserver_nostatic',
    'accounts',
    'stories',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # مسؤول عن خدمة ملفات Vite
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/dist'),
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ar-sa'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# --- إعدادات الملفات الثابتة (Vite Compatibility) ---
# نستخدم 'static/' لتجنب التضارب مع النظام، وسنتعامل مع الروابط في urls.py
STATIC_URL = 'static/' # اتركه هكذا ليتوقف خطأ الإعدادات
STATIC_ROOT = str(os.path.join(BASE_DIR, 'staticfiles'))
STATICFILES_DIRS = [
    str(os.path.join(BASE_DIR, 'frontend/dist')),
]

# تخزين WhiteNoise storage with Django 6 compatibility fix
# Use default storage - we'll serve files directly to avoid Django 6 pathlib issues
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# --- إعدادات Media ---
# إضافة السلاش في البداية '/' ضروري جداً لفك الاشتباك
MEDIA_URL = '/media/' 
MEDIA_ROOT = str(os.path.join(BASE_DIR, 'media'))

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

CORS_ALLOW_ALL_ORIGINS = DEBUG

CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv('CORS_ALLOWED_ORIGINS', 'http://localhost:5173,http://127.0.0.1:5173').split(',')
    if origin.strip()
]

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'Oda <no-reply@oda.com>')
ODA_SUPPORT_EMAIL = os.getenv('ODA_SUPPORT_EMAIL', 'support@oda.com')

FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:5173')