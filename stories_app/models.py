from django.db import models
from django.contrib.auth.models import User # إذا كنت تريد ربط القصة بمستخدم

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title