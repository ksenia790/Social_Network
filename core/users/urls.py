from django.urls import path
from .views import register, user_login, user_logout

app_name = 'users'

urlpatterns=[
    path('register/', register, name="register"),
    path('login/', user_login, name="user_login"),
]
