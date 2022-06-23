# Generated by Django 3.2 on 2022-06-23 15:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_tag', models.CharField(default='blog', max_length=250)),
                ('body', models.TextField(blank=True, null=True)),
                ('likes', models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]