from rest_framework import serializers

from stories.models import Story, Comment, Rating


class StorySerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    file_name = serializers.CharField(source='file_path.name', read_only=True)
    average_rating = serializers.SerializerMethodField()
    ratings_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = [
            'id',
            'title',
            'file_path',
            'file_name',
            'description',
            'author',
            'author_username',
            'status',
            'genre',
            'views_count',
            'likes_count',
            'average_rating',
            'ratings_count',
            'comments_count',
            'language',
            'tags',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'views_count', 'likes_count', 'created_at', 'updated_at']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_ratings_count(self, obj):
        return obj.ratings.count()

    def get_comments_count(self, obj):
        return obj.comments.filter(is_approved=True).count()


class CommentSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'story',
            'user',
            'user_username',
            'content',
            'is_approved',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'user', 'is_approved', 'created_at', 'updated_at']


class RatingSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    rating_display = serializers.CharField(source='get_rating_display', read_only=True)

    class Meta:
        model = Rating
        fields = [
            'id',
            'story',
            'user',
            'user_username',
            'rating',
            'rating_display',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

