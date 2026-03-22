from django.contrib import admin
from stories.models import Story, Comment, Rating


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'status', 'views_count', 'likes_count', 'average_rating_display', 'created_at']
    list_filter = ['genre', 'status', 'language']
    search_fields = ['title', 'description', 'author__username']
    readonly_fields = ['created_at', 'updated_at']

    def average_rating_display(self, obj):
        return obj.get_average_rating()
    average_rating_display.short_description = 'متوسط التقييم'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'story', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['content', 'user__username', 'story__title']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'story', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'story__title']
    readonly_fields = ['created_at', 'updated_at']
