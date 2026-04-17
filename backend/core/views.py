"""
Custom views that fix Django 6.0.4 pathlib compatibility issues.
"""

import os
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.conf import settings
from django.views.static import serve as original_serve
from pathlib import Path


def fixed_serve(request, path, document_root=None):
    """
    Fixed version of Django's serve view that handles PosixPath objects properly.
    This fixes the 'PosixPath' object has no attribute 'stat' error in Django 6.0.4.
    الإصدار 5: إضافة التحقق من اجتياز المسار (Path Traversal) لمنع الوصول لملفات خارج document_root
    """
    # Convert document_root to string if it's a Path object
    if document_root is not None:
        if hasattr(document_root, 'as_posix'):
            document_root = str(document_root)
        elif isinstance(document_root, Path):
            document_root = str(document_root)

    # الإصدار 5: التحقق من أن المسار المطلوب لا يخرج من document_root (منع Path Traversal)
    document_root_real = os.path.realpath(os.path.abspath(document_root))
    fullpath = os.path.realpath(os.path.abspath(os.path.join(document_root, path)))

    # رفض أي طلب يحاول الوصول لمسار خارج المجلد المسموح به
    if not fullpath.startswith(document_root_real + os.sep) and fullpath != document_root_real:
        return HttpResponseForbidden("Access denied: path traversal detected.")

    # Check if file exists
    if not os.path.exists(fullpath):
        raise Http404(f'"{path}" does not exist')

    # Check if it's a file (not directory)
    if not os.path.isfile(fullpath):
        raise Http404(f'"{path}" is not a file')

    # Get file content and MIME type
    try:
        with open(fullpath, 'rb') as f:
            content = f.read()

        # Determine content type
        content_type = 'application/octet-stream'
        if path.endswith('.js'):
            content_type = 'application/javascript'
        elif path.endswith('.css'):
            content_type = 'text/css'
        elif path.endswith('.png'):
            content_type = 'image/png'
        elif path.endswith('.jpg') or path.endswith('.jpeg'):
            content_type = 'image/jpeg'
        elif path.endswith('.gif'):
            content_type = 'image/gif'
        elif path.endswith('.svg'):
            content_type = 'image/svg+xml'
        elif path.endswith('.txt'):
            content_type = 'text/plain; charset=utf-8'
        elif path.endswith('.pdf'):
            content_type = 'application/pdf'
        elif path.endswith('.epub'):
            content_type = 'application/epub+zip'
        elif path.endswith('.docx'):
            content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        elif path.endswith('.ico'):
            content_type = 'image/x-icon'
        elif path.endswith('.woff2'):
            content_type = 'font/woff2'
        elif path.endswith('.woff'):
            content_type = 'font/woff'

        response = HttpResponse(content, content_type=content_type)
        return response

    except Exception as e:
        raise Http404(f'Error serving file: {e}')
