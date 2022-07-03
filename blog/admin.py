from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Contact


@admin.register(Post)
class BlogAdmin(SummernoteModelAdmin):
    """
    Class that populates fields when creating a post in the Django Admin Panel
    """
    list_display = ('title', 'author', 'post_date')
    summernote_fields = ('body')


admin.site.register(Comment)
admin.site.register(Contact)
