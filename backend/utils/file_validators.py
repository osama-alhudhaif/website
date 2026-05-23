"""
الإصدار 9: مُحقِّق مشترك لرفع الملفات
يتحقق من نوع الملف (MIME)، الامتداد، والحجم
يرفض الملفات الخطيرة مثل الملفات التنفيذية والسكريبتات
"""

import os
import mimetypes
from django.core.exceptions import ValidationError

# الحجم الأقصى للملف: 50 جيجابايت
MAX_FILE_SIZE_BYTES = 50 * 1024 * 1024 * 1024

# الامتدادات المسموح بها لملفات القصص
ALLOWED_STORY_EXTENSIONS = {'.pdf', '.doc', '.docx', '.txt', '.epub'}

# أنواع MIME المسموح بها لملفات القصص
ALLOWED_STORY_MIME_TYPES = {
    'application/pdf',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'text/plain',
    'application/epub+zip',
}

# امتدادات وأنواع MIME الخطيرة التي يجب رفضها دائماً
DANGEROUS_EXTENSIONS = {
    '.exe', '.bat', '.cmd', '.sh', '.bash', '.ps1', '.psm1', '.psd1',
    '.vbs', '.vbe', '.js', '.jse', '.wsf', '.wsh', '.msc', '.msi',
    '.msp', '.com', '.scr', '.hta', '.cpl', '.jar', '.py', '.rb',
    '.pl', '.php', '.asp', '.aspx', '.jsp', '.cgi', '.dll', '.so',
    '.dylib', '.bin', '.elf', '.deb', '.rpm', '.dmg', '.app',
}

DANGEROUS_MIME_TYPES = {
    'application/x-executable',
    'application/x-msdownload',
    'application/x-sh',
    'application/x-csh',
    'text/x-shellscript',
    'application/x-dosexec',
    'application/x-msdos-program',
    'application/java-archive',
    'application/x-java-archive',
}


def validate_story_file(file):
    """
    التحقق من صلاحية ملف القصة المرفوع:
    1. التحقق من الحجم (أقل من 50 جيجابايت)
    2. التحقق من الامتداد
    3. التحقق من نوع MIME
    4. رفض الملفات الخطيرة
    """
    # التحقق من الحجم
    if file.size > MAX_FILE_SIZE_BYTES:
        raise ValidationError(
            f'حجم الملف يتجاوز الحد الأقصى المسموح به ({MAX_FILE_SIZE_BYTES // (1024 * 1024 * 1024)} جيجابايت).'
        )

    # التحقق من الامتداد
    _, ext = os.path.splitext(file.name.lower())

    if ext in DANGEROUS_EXTENSIONS:
        raise ValidationError(
            f'نوع الملف "{ext}" غير مسموح به لأسباب أمنية.'
        )

    if ext not in ALLOWED_STORY_EXTENSIONS:
        allowed = ', '.join(sorted(ALLOWED_STORY_EXTENSIONS))
        raise ValidationError(
            f'امتداد الملف "{ext}" غير مدعوم. الامتدادات المسموح بها: {allowed}'
        )

    # التحقق من نوع MIME
    mime_type, _ = mimetypes.guess_type(file.name)
    if mime_type:
        if mime_type in DANGEROUS_MIME_TYPES:
            raise ValidationError(
                f'نوع الملف "{mime_type}" غير مسموح به لأسباب أمنية.'
            )
        if mime_type not in ALLOWED_STORY_MIME_TYPES:
            raise ValidationError(
                f'نوع MIME "{mime_type}" غير مدعوم لملفات القصص.'
            )

    return file
