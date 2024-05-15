from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response

from .models import Post, Session, Setup
from .permissions import IsOwnerOrAdminOrReadOnly
from .serializers import PostSerializer, SessionSerializer, SetupSerializer


# View All/ Add/ Delete/ Update Session objects for DRF admins
class SessionViewset(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View All/ Add/ Delete/ Update Post objects for DRF admins
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View All/ Add/ Delete/ Update Setup objects for DRF admins
class SetupViewset(viewsets.ModelViewSet):
    queryset = Setup.objects.all()
    serializer_class = SetupSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserSetupViewset(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = SetupSerializer
    queryset = Setup.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
