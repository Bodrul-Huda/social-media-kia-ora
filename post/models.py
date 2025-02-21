from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    liked_users = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    mentioned_users = models.ManyToManyField(User, related_name="mentioned_in_posts", blank=True)
    
    POST_TYPES = [("text", "Text"), ("image", "Image"), ("video", "Video")]
    post_type = models.CharField(max_length=10, choices=POST_TYPES, default="text")
    image = models.ImageField(upload_to="blog_images/", null=True, blank=True)
    video = models.FileField(upload_to="videos/", null=True, blank=True)

    shared_post = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="shared_by")
    tags = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Post by {self.author.username} - {self.created_at.strftime('%Y-%m-%d')}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"
