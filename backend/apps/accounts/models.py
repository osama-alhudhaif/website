from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # الحقول المطلوبة من ملف READER و WRITER في الـ SQL
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    level = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, default='active')

    class Role(models.TextChoices):
        FOUNDER = 'FOUNDER', 'مؤسس'
        HIGH_ADMIN = 'HIGH_ADMIN', 'ادمن عالي'
        REGULAR = 'REGULAR', 'عادي'
        READER = 'READER', 'حساب قاري'
        WRITER = 'WRITER', 'حساب كاتب'
        MUAASIS = 'MUAASIS', 'المؤسس'
        EDU_CENTER = 'EDU_CENTER', 'المركز التعليمي'
        TEACHER = 'TEACHER', 'معلم'
        STUDENT = 'STUDENT', 'طالب'
        GUEST = 'GUEST', 'زائر'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.REGULAR)