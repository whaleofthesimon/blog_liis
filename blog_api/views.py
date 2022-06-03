from rest_framework import generics, permissions
from blog_api.models import Article, CustomUser
from blog_api.permissions import IsNonAuthenticated, IsAuthor, IsCurrentAuthorUser
from blog_api.serializers import TimelineSerializer, ArticleCreationSerializer, RegistrationSerializer, \
    UserAdministrationSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsNonAuthenticated]


class TimelineView(generics.ListAPIView):
    serializer_class = TimelineSerializer

    def get_queryset(self):
        user = self.request.user
        if user.__str__() == 'AnonymousUser':
            return Article.objects.filter(access=1)
        return Article.objects.all()


class ArticleCreationView(generics.CreateAPIView):
    serializer_class = ArticleCreationSerializer
    permission_classes = [IsAuthor]


class ArticleEditingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCurrentAuthorUser]
    serializer_class = ArticleCreationSerializer
    queryset = Article.objects.all()


class UserAdministrationView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserAdministrationSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = CustomUser.objects.all()


class UserAdministrationListView(generics.ListAPIView):
    serializer_class = UserAdministrationSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = CustomUser.objects.all()
