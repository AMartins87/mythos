from django.contrib import admin
from django.urls import path, include
from .views import HomeView, StoryView, AddPostView, AddCommentView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', StoryView.as_view(), name="blog"),
    path('new-post/', AddPostView.as_view(), name="new-post"),
    path('like/<int:pk>', views.LikeView, name="like_post"),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name="comment"),
]
