# Generated by Django 4.2.7 on 2023-11-14 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_tag_alter_like_unique_together_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
