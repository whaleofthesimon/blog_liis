from django.contrib import admin
from blog_api.models import CustomUser, Article

admin.site.register(CustomUser)
admin.site.register(Article)
