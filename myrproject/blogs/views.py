from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Blog, Comment
from .serializer import BlogSerializer, CommentSerializer
from .filters import BlogFilter
from .permission import BlogPermission
from api.paginations import Mycursorpaginatation, Mylimitoffset   # adjust if needed


# ✅ BLOG LIST + CREATE (with caching)
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter

    def list(self, request, *args, **kwargs):
        cache_key = "blogs_list"

        cached_data = cache.get(cache_key)
        if cached_data:
            print("⚡ CACHE HIT")
            return Response(cached_data)

        print("❌ CACHE MISS (DB HIT)")
        response = super().list(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=60)
        return response   # ✅ FIXED


# ✅ BLOG VIEWSET (FULL CRUD)
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = Mycursorpaginatation
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter
    permission_classes = [BlogPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ✅ COMMENTS VIEWSET
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = Mylimitoffset


# ✅ OPTIONAL: SIMPLE COMMENTS API
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer