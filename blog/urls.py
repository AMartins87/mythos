from django.urls import path, include
from .views import HomeView, StoryView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', StoryView.as_view(), name="blog"),
    path('new-post/', AddPostView.as_view(), name="new-post"),
]
