from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse
from .models import Post
from .forms import PostForm

class PostListView(ListView):

    template_name = 'blog/list.html'
    queryset = Post.objects.all()
    context_object_name = 'blogs'

class PostDetailView(DetailView):

    template_name = 'blog/detail.html'
    context_object_name = 'blog'

    def get_queryset(self):
        # self.kwargs['pk] or self.kwargs.get('pk)
        return Post.objects.filter(id=self.kwargs.get('pk')) 
    
class PostCreateView(CreateView):

    template_name = 'blog/create.html'
    form_class = PostForm
    success_url = '/'

class PostUpdateView(UpdateView):

    template_name = 'blog/update.html'
    form_class = PostForm
    success_url = '/'

    def get_queryset(self):
        # self.kwargs['pk] or self.kwargs.get('pk)
        return Post.objects.filter(id=self.kwargs.get('pk')) 

class PostDeleteView(DeleteView):

    template_name = 'blog/delete.html'
    success_url = '/'
    context_object_name = 'blog'

    def get_queryset(self):
        # self.kwargs['pk] or self.kwargs.get('pk)
        return Post.objects.filter(id=self.kwargs.get('pk')) 
