from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from blog_api.models import Article, CustomUser
from blog_api.validators import FullCommonValidator

UserModel = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def validate_password(self, value):
        try:
            password_validators = [FullCommonValidator(), ]
            validators.validate_password(value, password_validators=password_validators)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):
        user = UserModel.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class UserAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'is_superuser', 'is_author')
