from django.urls import path, include
from rest_framework import routers

from blog_api.views import *

app_name = 'blog_api'

router = routers.SimpleRouter()
router.register(r'articles', BlogViewSet, basename='article')

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('', include(router.urls))

]
