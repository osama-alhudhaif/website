from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User
from stories.models import Story


class StoryTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='writer', password='TestPass123!', is_active=True, role='WRITER'
        )
        self.other_user = User.objects.create_user(
            username='reader', password='TestPass123!', is_active=True, role='READER'
        )
        self.client.force_authenticate(user=self.user)

    def _make_story(self, title='قصة اختبار', story_status='published'):
        file = SimpleUploadedFile("story.txt", b"content", content_type="text/plain")
        return Story.objects.create(
            title=title, author=self.user,
            status=story_status, genre='خيال علمي', file_path=file,
        )

    def test_list_stories_requires_auth(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/v1/stories/stories/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_stories_authenticated(self):
        self._make_story()
        response = self.client.get('/api/v1/stories/stories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_stories(self):
        self._make_story(title='قصة الفضاء')
        self._make_story(title='رحلة البحر')
        response = self.client.get('/api/v1/stories/stories/?search=الفضاء')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data)
        titles = [s['title'] for s in results]
        self.assertIn('قصة الفضاء', titles)
        self.assertNotIn('رحلة البحر', titles)

    def test_story_view_count_increments(self):
        story = self._make_story()
        initial_views = story.views_count
        self.client.get(f'/api/v1/stories/stories/{story.id}/')
        story.refresh_from_db()
        self.assertEqual(story.views_count, initial_views + 1)

    def test_only_author_can_delete(self):
        story = self._make_story()
        self.client.force_authenticate(user=self.other_user)
        response = self.client.delete(f'/api/v1/stories/stories/{story.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_can_delete_own_story(self):
        story = self._make_story()
        response = self.client.delete(f'/api/v1/stories/stories/{story.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_my_stories_filter(self):
        self._make_story(title='قصتي', story_status='draft')
        Story.objects.create(
            title='قصة أخرى', author=self.other_user, status='published',
            genre='رومانسي', file_path=SimpleUploadedFile("f.txt", b"x")
        )
        response = self.client.get('/api/v1/stories/stories/?my_stories=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data)
        author_ids = {s['author'] for s in results}
        self.assertIn(self.user.id, author_ids)
        self.assertNotIn(self.other_user.id, author_ids)
