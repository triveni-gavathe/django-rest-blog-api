from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BlogViewSet, CommentViewSet, BlogListCreateView

router = DefaultRouter()
router.register('blogs', BlogViewSet, basename='blog')          # /api/blogs/
router.register('comments', CommentViewSet, basename='comment')  # /api/blogs/comments/

urlpatterns = [
    path('', include(router.urls)),         # ✅ main API
    path('list/', BlogListCreateView.as_view()),  # ✅ optional cached list
]