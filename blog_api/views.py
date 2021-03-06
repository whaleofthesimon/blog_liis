from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from blog_api.models import Article
from blog_api.permissions import IsAuthor, IsCurrentAuthorUser
from blog_api.serializers import RegistrationSerializer, BlogSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [~IsAuthenticated, ]


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthor, ]
        elif self.action in ('update', 'destroy', 'retrieve'):
            self.permission_classes = [IsCurrentAuthorUser, ]
        return super(BlogViewSet, self).get_permissions()

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Article.objects.filter(is_private=False)
        return Article.objects.all()

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(author=current_user)
