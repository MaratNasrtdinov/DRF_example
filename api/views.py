from rest_framework import generics, permissions, viewsets
from . import serializers
from django.contrib.auth.models import User
from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]


class PostList(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            self.permission_classes = [permissions.IsAdminUser]
        if self.action in ('create',):
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return super(PostList, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentList(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            self.permission_classes = [permissions.IsAdminUser]
        if self.action in ('create',):
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return super(CommentList, self).get_permissions()

