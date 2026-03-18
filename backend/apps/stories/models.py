from django.db import models
from accounts.models import User

class Story(models.Model):
    # الحقول من ملف الـ SQL
    title = models.TextField()
    file_path = models.FileField(upload_to='stories/%Y/%m/%d/')
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    status = models.CharField(max_length=100)
    genre = models.CharField(max_length=255)
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    language = models.CharField(max_length=100, null=True, blank=True)
    tags = models.TextField(null=True, blank=True) # تم تحويل SET إلى TEXT كما في ملف psql
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)