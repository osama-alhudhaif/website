from django.db import models


# website/stories/models.py

from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان القصة")
    author = models.CharField(max_length=100, verbose_name="المؤلف")
    content = models.TextField(verbose_name="نص القصة الكامل")
    translation_status = models.BooleanField(default=False, verbose_name="مترجمة آلياً")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "قصة"
        verbose_name_plural = "قصص"