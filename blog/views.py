from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


# def home(request):
#     return render(request, 'index.html')
class HomeView(ListView):
    model = Post
    template_name = 'index.html'


class StoryView(DetailView):
    model = Post
    template_name = 'stories.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
