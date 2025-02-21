from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from post.models import Post
# from django import  
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse




class home(ListView):
  model = Post 
  template_name = 'index.html' 
  context_object_name = 'posts'

  def get_queryset(self):
        posts = Post.objects.filter(is_published=True).order_by('-created_at')
        for post in posts:
            post.show_more = len(post.content.split()) > 30  # Add attribute dynamically
        return posts
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_buttons'] = False  
        return context


# def home(request):
#   return render(request, 'index.html')