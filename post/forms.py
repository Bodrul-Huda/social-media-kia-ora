# from django import forms
from django import forms
from . import models
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User


class Posts_form(forms.ModelForm):
   class Meta:
      model = models.Post
      fields = ['title', 'content', 'image', 'video']
      widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'}),
            'content': forms.Textarea(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'}),
            'video': forms.FileInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'}),
         }
      



class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "w-full p-2 border rounded", "rows": 3, "placeholder": "Write a comment..."}),
        }