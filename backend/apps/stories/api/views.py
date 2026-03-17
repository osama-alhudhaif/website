from rest_framework import viewsets, permissions

from stories.models import Story
from .serializers import StorySerializer


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        queryset = Story.objects.select_related('author').all()
        genre = self.request.query_params.get('genre')
        language = self.request.query_params.get('language')
        author_id = self.request.query_params.get('author')

        if genre:
            queryset = queryset.filter(genre__iexact=genre)
        if language:
            queryset = queryset.filter(language__iexact=language)
        if author_id:
            queryset = queryset.filter(author_id=author_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

