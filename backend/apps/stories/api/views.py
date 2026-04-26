from rest_framework import viewsets, permissions, generics, status, serializers, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db import models as db_models

from stories.models import Story, Comment, Rating, StoryLike
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
    search_fields = ['title', 'description', 'author__username', 'genre']
    ordering_fields = ['created_at', 'views_count', 'title']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Story.objects.select_related('author').filter(status='published')
        genre = self.request.query_params.get('genre')
        if genre:
            queryset = queryset.filter(genre__iexact=genre)
        # إذا طلب المستخدم قصصه الخاصة (مسودة + منشورة)
        if self.request.query_params.get('my_stories'):
            queryset = Story.objects.select_related('author').filter(author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count += 1
        instance.save()
        return Response(self.get_serializer(instance).data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        story = self.get_object()
        like, created = StoryLike.objects.get_or_create(user=request.user, story=story)
        if not created:
            like.delete()
            story.likes_count = db_models.F('likes_count') - 1
            story.save(update_fields=['likes_count'])
            story.refresh_from_db()
            return Response({'liked': False, 'likes_count': story.likes_count})
        story.likes_count = db_models.F('likes_count') + 1
        story.save(update_fields=['likes_count'])
        story.refresh_from_db()
        return Response({'liked': True, 'likes_count': story.likes_count})

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def is_liked(self, request, pk=None):
        story = self.get_object()
        liked = StoryLike.objects.filter(user=request.user, story=story).exists()
        return Response({'liked': liked})


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(story_id=self.kwargs['story_id'], is_approved=True)

    def perform_create(self, serializer):
        story_id = self.kwargs['story_id']
        # الإصدار 10: استخدام get_object_or_404 بدلاً من Story.objects.get لإرجاع 404 عند عدم الوجود
        story = get_object_or_404(Story, id=story_id)
        serializer.save(user=self.request.user, story=story)


class RatingListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(story_id=self.kwargs['story_id'])

    def perform_create(self, serializer):
        story_id = self.kwargs['story_id']
        # الإصدار 10: استخدام get_object_or_404 بدلاً من Story.objects.get لإرجاع 404 عند عدم الوجود
        story = get_object_or_404(Story, id=story_id)
        if Rating.objects.filter(story=story, user=self.request.user).exists():
            raise serializers.ValidationError('لقد قيّمت هذه القصة مسبقاً')
        serializer.save(user=self.request.user, story=story)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(is_approved=True)

    def perform_update(self, serializer):
        # Only allow updating if the user is the author
        if serializer.instance.user != self.request.user:
            raise permissions.PermissionDenied("You can only edit your own comments.")
        serializer.save()

    def perform_destroy(self, instance):
        # Only allow deletion if the user is the author
        if instance.user != self.request.user:
            raise permissions.PermissionDenied("You can only delete your own comments.")
        instance.delete()


class UserRatingAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, story_id):
        try:
            rating = Rating.objects.get(story_id=story_id, user=request.user)
            return Response(RatingSerializer(rating).data)
        except Rating.DoesNotExist:
            return Response({'rating': None})
