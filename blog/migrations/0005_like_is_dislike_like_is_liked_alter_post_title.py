# Generated by Django 4.2.7 on 2023-11-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_text_post_content_remove_post_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='like',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
