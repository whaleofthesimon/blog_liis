from django.urls import path
from blog_api.views import *

app_name = 'blog_api'
urlpatterns = [
    path('timeline/', TimelineView.as_view()),
    path('article-create/', ArticleCreationView.as_view()),
    path('article-edit/<int:pk>/', ArticleEditingView.as_view()),
    path('registration/', RegistrationView.as_view()),
    path('administrate-users/<int:pk>/', UserAdministrationView.as_view()),
    path('administrate-users/all/', UserAdministrationListView.as_view()),
]
