from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserUpdateForm
from post.models import Post
from django.contrib import messages

class UserRegistration(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('User_profile')  
    template_name = 'signUp.html'

    def form_valid(self, form):
        """Ensure the password is hashed, save the user, and log them in."""
        user = form.save()
        login(self.request, user)  
        messages.success(self.request, "Account created successfully! Welcome 🎉")
        return redirect("User_profile")
    def form_invalid(self, form):
        messages.error(self.request, "Registration failed. Please correct the errors below.")
        return super().form_invalid(form)


class User_profile(LoginRequiredMixin, ListView):
    model = Post
    template_name = "user_profile.html"
    context_object_name = "posts"

    def get_queryset(self):
        """Return only blogs created by the logged-in user and are published."""
        return Post.objects.filter(is_published=True, author=self.request.user)

    def get_context_data(self, **kwargs):
        """Add additional context data."""
        context = super().get_context_data(**kwargs)
        context["show_buttons"] = True
        context["user_profile"] = self.request.user
        return context

from django.contrib.auth.hashers import make_password

class User_update(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('User_profile')
    template_name = 'signUp.html'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        """Ensure user is updating their own profile."""
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def form_valid(self, form):
        """Ensure username uniqueness before saving."""
        user = form.save(commit=False)

        # Check if another user already has this username (case-insensitive)
        if User.objects.exclude(pk=user.pk).filter(username__iexact=form.cleaned_data['username']).exists():
            form.add_error('username', "This username is already taken. Please choose another.")
            messages.error(self.request, "Username is already taken. Try a different one.")
            return self.form_invalid(form)

        user.save()

        messages.success(self.request, "Profile updated successfully! ✅")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Update failed. Please correct the errors below.")
        return super().form_invalid(form)