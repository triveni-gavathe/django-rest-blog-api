# from django.shortcuts import render,get_object_or_404
# from django.http import JsonResponse
# from student.models import Stundent
# from .Serializer import StudentSerializer,EmpolyeeSerializer
# from rest_framework.response import Response
# from   rest_framework import status
# from rest_framework.decorators import api_view 
# from rest_framework.views import APIView
# from employees.models import Employee
# from django.http import Http404
# from rest_framework import mixins,generics
# from rest_framework import viewsets
# from blogs.models import Blog,Comment
# from blogs.serializer import BlogSerializer,CommentSerializer
# from .paginations import custompagination,Mycursorpaginatation,Mylimitoffset
# from django_filters.rest_framework import DjangoFilterBackend
# from .filters import EmployeeFilter,BlogFilter
# from rest_framework.filters import SearchFilter,OrderingFilter
# from django.contrib.auth.models import User
# from rest_framework.permissions import IsAuthenticated
# from blogs.permission import BlogPermission
# from django.core.cache import cache
# # Create your views here.



 
# class BlogView(generics.ListCreateAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
    
#     filter_backends = [DjangoFilterBackend]
#     filterset_class =BlogFilter
#     def list(self, request, *args, **kwargs):   #get i 
#         print("FILTER PARAMS:", request.GET)
        
#         cache_key='blogs_list'
#         cached_data=cache.get(cache_key)
#         if cached_data:
#             print("⚡ CACHE HIT")
#             return Response(cached_data)
#         print("❌ CACHE MISS (DB HIT)")
#         response=super().list(request,*args,**kwargs)
#         cache.set(cache_key,response.data,timeout=60)
        
#         return super().list(request, *args, **kwargs)       
#     def get_queryset(self):
#         print("VIEW HIT ✅")
#         return super().get_queryset()    
#     def get_queryset(self):
#         return Blog.objects.filter(blog_title__icontains="test")
   
    
# class CommentsView(generics.ListCreateAPIView):
#     queryset=Comment.objects.all()
#     serializer_class=CommentSerializer
  
# class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
#     lookup_field='pk'
# # class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset=Comment.objects.all()
# #     serializer_class=CommentSerializer
# #     lookup_field='pk'


# class BlogDetailView(viewsets.ModelViewSet):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
#     pagination_class=Mycursorpaginatation
#     filter_backends = [DjangoFilterBackend]   # ✅ ADD THIS
#     filterset_class = BlogFilter   
#     permission_classes=[BlogPermission] 
#     def perform_create(self,serializer):
#         serializer.save(user=self.request.user)  #its save the into data or the current user 
       
# class CommentDetailsView(viewsets.ModelViewSet):
#     queryset=Comment.objects.all()
#     serializer_class=CommentSerializer       
#     pagination_class=Mylimitoffset
    
