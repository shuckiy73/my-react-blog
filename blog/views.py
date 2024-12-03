from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.core.mail import send_mail
from django.db.models import Count
from blog.models import Post
from taggit.models import Tag
from .serializers import BlogSerializer
from rest_framework import serializers 
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Post
from .serializers import BlogSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

# Представление для перенаправления на список постов
def some_view(request):
    # Перенаправление на список постов
    return redirect('blog:list_view')

# Представление для списка всех постов
class PostListView(ListAPIView):
    queryset = Post.published.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny, )

# Представление для деталей поста
class BlogDetailView(RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

# Представление для избранных постов
class BlogFeaturedView(ListAPIView):
    queryset = Post.objects.filter(featured=True)
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny, )

# Представление для постов по категории
class BlogCategoryView(ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(category__iexact=category).order_by('-date_created')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
from django.utils import timezone
from django.db import models

now = timezone.now()  # get the current time

class PostListView(ListAPIView):
    queryset = Post.published.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny, )

class BlogDetailView(RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogFeaturedView(ListAPIView):
    queryset = Post.objects.filter(featured=True)
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny, )

class BlogCategoryView(ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(category__iexact=category).order_by('-date_created')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
