from django.shortcuts import render
from rest_framework import viewsets

from .models import Post, Comment, Category, Tag, Like
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, TagSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


posts = Post.objects.all()
for post in posts:
    likes_count = post.like_set.count()


def post_details(self):
    post = Post.objects.all()
    comments = post.comment_set.all()
    return comments


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
