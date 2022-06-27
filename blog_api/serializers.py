from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validators
from rest_framework import serializers

from blog_api.models import Article

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def validate_password(self, value):
        validators.validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('topic', 'filling', 'author', 'is_private')
        read_only_fields = ('author',)
