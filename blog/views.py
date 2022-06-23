from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from .forms import PostForm


# def home(request):
#     return render(request, 'index.html')
class HomeView(ListView):
    model = Post
    template_name = 'index.html'
