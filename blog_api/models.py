from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    roles = (
        ('subscriber', 'Подписчик'),
        ('author', 'Автор')
    )
    user_role = models.CharField(verbose_name='Роль пользователя', choices=roles, default='subscriber', max_length=32)

    def __str__(self):
        return self.email


User = get_user_model()


class Article(models.Model):
    topic = models.CharField(verbose_name='Заголовок статьи', unique=True, max_length=256)
    filling = models.TextField(verbose_name='Тело статьи')
    article_access_types = (
        ('public', 'Публичная статья'),
        ('for_subscribers', 'Только для подписчиков')
    )
    access = models.CharField(verbose_name='Доступность статьи', choices=article_access_types, max_length=32)
    author = models.ForeignKey(User, verbose_name='Автор статьи', on_delete=models.CASCADE)
