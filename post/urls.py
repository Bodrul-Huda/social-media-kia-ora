
from django.urls import path
from .import views


urlpatterns = [
    
    path('post_create/', views.Post_create.as_view(), name='Post_create'),
    path('delete/<int:pk>/', views.Post_delete.as_view(), name='Post_delete'),
    path('post_update/<int:pk>/', views.Post_update.as_view(), name='Post_update'),  
    path("search/", views.PostSearch.as_view(), name="search"),
    path('toggle_like/<int:pk>/like/', views.ToggleLikeView.as_view(), name='toggle_like'),
    path("post_details/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),  

    
]