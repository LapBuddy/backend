from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .models import Session, Post, Setup
from .serializers import SessionSerializer, PostSerializer, SetupSerializer

# View All/ Add/ Delete/ Update Session objects for DRF admins
class SessionViewset(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

# View All/ Add/ Delete/ Update Post objects for DRF admins
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

# View All/ Add/ Delete/ Update Setup objects for DRF admins
class SetupViewset(viewsets.ModelViewSet):
    queryset = Setup.objects.all()
    serializer_class = SetupSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]