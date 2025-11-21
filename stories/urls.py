# website/stories/urls.py

from rest_framework.routers import DefaultRouter
from .views import StoryViewSet 

router = DefaultRouter()
router.register(r'stories', StoryViewSet)

urlpatterns = router.urls