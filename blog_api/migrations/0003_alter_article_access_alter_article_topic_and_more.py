# Generated by Django 4.0.4 on 2022-06-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0002_customuser_is_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='access',
            field=models.IntegerField(choices=[(1, 'Публичная статья'), (2, 'Только для подписчиков')], verbose_name='Доступность статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.CharField(max_length=256, unique=True, verbose_name='Заголовок статьи'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='Режим автора'),
        ),
    ]