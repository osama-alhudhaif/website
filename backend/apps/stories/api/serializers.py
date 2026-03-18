from rest_framework import serializers

from stories.models import Story


class StorySerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    file_name = serializers.CharField(source='file_path.name', read_only=True)

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
            'language',
            'tags',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'views_count', 'likes_count', 'created_at', 'updated_at']

