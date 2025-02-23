from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from . import models, forms
# from django import  
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post



# # Create your views here.


# # -------------------- Blogs CRUD operation


# # create  post in class view

class Post_create(LoginRequiredMixin, CreateView):
    model = models.Post
    form_class = forms.Posts_form
    success_url = reverse_lazy('home')
    template_name = 'postForm.html'

    def form_valid(self, form):
        """Assign the logged-in user as the author before saving the form."""
        form.instance.author = self.request.user  
        messages.success(self.request, "Your post has been created successfully!")
        return super().form_valid(form)
  


class Post_delete(LoginRequiredMixin, DeleteView):
    model = models.Post  
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('User_profile')
    template_name = 'deleteUrl.html'

    def delete(self, request, *args, **kwargs):
        blog = get_object_or_404(models.Post, pk=self.kwargs['pk'])

        # Check if the logged-in user is the author
        if blog.author != request.user:
            messages.error(request, "You are not allowed to delete this post.")
            return redirect('home')  

        messages.success(request, "Your post has been deleted successfully.")
        return super().delete(request, *args, **kwargs)




class Post_update(LoginRequiredMixin, UpdateView):
    model = models.Post  
    fields = [ 'content', 'image', 'video' ]
    success_url = reverse_lazy('User_profile')
    template_name = 'postForm.html'
    pk_url_kwarg = 'pk'

    def dispatch(self, request, *args, **kwargs):
        """Check if the logged-in user is the author before allowing update."""
        post = get_object_or_404(models.Post, pk=self.kwargs['pk'])

        if post.author != request.user:
            messages.error(request, "You are not authorized to edit this post.")
            return redirect('home')  

        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        """Ensure the form is valid before saving."""
        messages.success(self.request, "Your post has been updated successfully.")
        return super().form_valid(form)
    




class PostDetailView(DetailView):
    model = models.Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by("-created_at")  # Fetch comments
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """Handle comment submission."""
        self.object = self.get_object()
        form = CommentForm(request.POST)      

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=self.object.pk)

        return self.get(request, *args, **kwargs)




class ToggleLikeView(LoginRequiredMixin, View):
    """Handles Like/Unlike functionality."""
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(models.Post, pk=self.kwargs['pk'])

        if post.liked_users.filter(id=request.user.id).exists():
            post.liked_users.remove(request.user)  # Unlike
            
        else:
            post.liked_users.add(request.user)  # Like
            

        return HttpResponseRedirect(reverse("home"))


class PostSearch(ListView):
    model = models.Post
    template_name = "index.html"  # Template for displaying blogs
    context_object_name = "posts"  # Name for accessing in the template

    def get_queryset(self):
        """Filter blogs based on search query."""
        query = self.request.GET.get("q")  # Get search query from URL
        if query:
            return models.Post.objects.filter(content__icontains=query)  # Case-insensitive search
        return models.Post.objects.all()




class PostListView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True)
        sort_order = self.request.GET.get("sort_order", "newest")
        media_type = self.request.GET.get("media_type", "all")
        user = self.request.GET.get("user", "")

        if media_type == "withImages":
            queryset = queryset.filter(image__isnull=False)
        elif media_type == "withoutImages":
            queryset = queryset.filter(image__isnull=True)

        if user:
            queryset = queryset.filter(author__username__icontains=user)

        if sort_order == "oldest":
            queryset = queryset.order_by("created_at")
        else:
            queryset = queryset.order_by("-created_at")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context
