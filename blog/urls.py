from django.urls import path
from .views import (HomeView, StoryView, AddPostView,
                    AddCommentView, LikeView, UpdatePostView,
                    DeletePostView, ContactView)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', StoryView.as_view(), name="blog"),
    path('new-post/', AddPostView.as_view(), name="new-post"),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('blog/delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name="comment"),
    path('contact/', ContactView.as_view(), name="contact"),
]
