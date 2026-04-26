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

    def __str__(self):
        return self.title

    def get_average_rating(self):
        """الحصول على متوسط التقييم"""
        ratings = self.ratings.all()
        if not ratings:
            return 0
        return sum(r.rating for r in ratings) / ratings.count()


class Comment(models.Model):
    """موديل التعليقات على القصص"""
    story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"تعليق {self.user.username} على {self.story.title}"


class StoryLike(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['story', 'user']

    def __str__(self):
        return f"{self.user.username} أعجب بـ {self.story.title}"


class Rating(models.Model):
    """موديل تقييم القصص"""

    class RatingValue(models.IntegerChoices):
        ONE = 1, '1 نجمة'
        TWO = 2, '2 نجمة'
        THREE = 3, '3 نجوم'
        FOUR = 4, '4 نجوم'
        FIVE = 5, '5 نجوم'

    story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.IntegerField(choices=RatingValue.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['story', 'user']
        ordering = ['-created_at']

    def __str__(self):
        return f"تقييم {self.user.username} لـ {self.story.title}: {self.rating}"