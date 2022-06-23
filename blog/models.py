from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250, default="blog")
    body = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="blog_post")

    def __str__(self):
        return self.title
