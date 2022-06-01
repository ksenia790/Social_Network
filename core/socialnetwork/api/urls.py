from django.urls import path
from .views import (
    PostListAPIView, 
    PostDetailAPIView, 
    PostCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
    CommentCreateAPIView,
    )


app_name = 'socialnetwork' 

urlpatterns = [
    path('comments/', CommentListAPIView.as_view(), name="comments"),
    path('posts/', PostListAPIView.as_view(), name="post_list"),
    path('post/create/', PostCreateAPIView.as_view(), name="create"),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name="thread"),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name="detail"),
    path('posts/<slug:slug>/create_comment', CommentCreateAPIView.as_view(), name="post_comments"),
]
