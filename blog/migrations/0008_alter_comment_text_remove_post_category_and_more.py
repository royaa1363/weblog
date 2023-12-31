# Generated by Django 4.2.7 on 2023-11-14 21:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=256),
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user',)},
        ),
        migrations.RemoveField(
            model_name='like',
            name='is_dislike',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(null=True, to='blog.category'),
        ),
    ]
