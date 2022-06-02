from django.urls import path
from . import views
from users.views import user_logout

app_name = 'socialnetwork'

urlpatterns=[
    path('', views.post_list, name="post_list"),
    path('add_post/', views.CreatePost.as_view(), name="add_post"),
    path('like/', views.like_post, name="like_post"),
    path('logout/', user_logout, name='logout'),
    path('<slug:post>/', views.post_detail, name="post_detail"),
    path('comment/reply/', views.reply_page, name="reply"),
]
