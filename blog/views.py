from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView,
                                  CreateView, DeleteView, UpdateView)
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Post, Comment, Contact
from .forms import PostForm, CommentForm, ContactForm


class HomeView(ListView):
    model = Post
    template_name = 'index.html'


class StoryView(DetailView):
    model = Post
    template_name = 'stories.html'

    def get_context_data(self, *args, **kwargs):
        context = super(StoryView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False

        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    """
    Adding a new story view
    """
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ('title', 'body')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'

    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    """
    Adding a comment to a post view
    """
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    success_url = reverse_lazy('home')


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog', args=[str(pk)]))


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'

    success_url = reverse_lazy('home')
