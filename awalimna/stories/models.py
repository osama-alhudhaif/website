from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

"""
راح اصمم هنا كل من
1- Story/Novel (الرواية/القصة)
2- Chapter (الفصل)
3- Genre (التصنيف/النوع)
"""

# تصميم شكل القصة
class Story(models.Model):
    id = models.AutoField(primary_key=True) #int only
    title = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
