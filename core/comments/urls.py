from django.urls import path
from . import views

app_name = 'comments'

urlpatterns=[
    path('comment/reply/', views.reply_page, name="reply"),
]
