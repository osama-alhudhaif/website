from rest_framework import viewsets, permissions, generics, status, serializers, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from stories.models import Story, Comment, Rating
from .serializers import StorySerializer, CommentSerializer, RatingSerializer


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'author__username', 'genre', 'tags']
    ordering_fields = ['created_at', 'views_count', 'likes_count', 'title']
    ordering = ['-created_at']

    def get_queryset(self):
        # قصص المستخدم الخاصة (مسودة + منشورة)
        if self.request.query_params.get('my_stories'):
            return Story.objects.select_related('author').filter(author=self.request.user)

        queryset = Story.objects.select_related('author').filter(status='published')
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(story_id=self.kwargs.get('story_id'), is_approved=True)

    def perform_create(self, serializer):
        if not self.request.user.has_active_subscription():
            raise permissions.PermissionDenied('يجب الاشتراك لإضافة تعليق')
        try:
            story = Story.objects.get(id=self.kwargs.get('story_id'))
        except Story.DoesNotExist:
            raise serializers.ValidationError('القصة غير موجودة')
        serializer.save(user=self.request.user, story=story)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)


class RatingListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(story_id=self.kwargs.get('story_id'))

    def perform_create(self, serializer):
        if not self.request.user.has_active_subscription():
            raise permissions.PermissionDenied('يجب الاشتراك لتقييم القصص')
        try:
            story = Story.objects.get(id=self.kwargs.get('story_id'))
        except Story.DoesNotExist:
            raise serializers.ValidationError('القصة غير موجودة')
        if Rating.objects.filter(story=story, user=self.request.user).exists():
            raise serializers.ValidationError('لقد قمت بتقييم هذه القصة بالفعل')
        serializer.save(user=self.request.user, story=story)
