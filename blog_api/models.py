from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from blog_api.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    is_author = models.BooleanField(verbose_name='Режим автора', default=False)

    def __str__(self):
        return self.email


User = get_user_model()


class Article(models.Model):
    topic = models.CharField(verbose_name='Заголовок статьи', unique=True, max_length=256)
    filling = models.TextField(verbose_name='Тело статьи')
    article_access_types = (
        (1, 'Публичная статья'),
        (2, 'Только для подписчиков')
    )
    access = models.IntegerField(verbose_name='Доступность статьи', choices=article_access_types)
    author = models.ForeignKey(User, verbose_name='Автор статьи', on_delete=models.CASCADE)
