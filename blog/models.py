from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=50)
    title_tag = models.CharField(max_length=50, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    body = models.TextField(blank=True, null=True)
    story_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name="blog_post", blank=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        """
        Method to tell Django how to calculate the canonical URL
        """
        return reverse('home')

    def total_likes(self):
        """Counts likes"""
        return self.likes.count()


class Comment(models.Model):
    """Comments model"""
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return '%s - %s' % (self.post.title, self.name)
        return f"Comment {self.body} by {self.name}"


class Contact(models.Model):
    """Contact model"""
    name = models.CharField(max_length=50, default="")
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        """
        Allows to review the contact model as email on admin dashboard
        """
        return self.email
