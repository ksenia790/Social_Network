from django.urls import path
from .views import UserCreateOrListView, GetToken

app_name = 'users'

urlpatterns = [
    path('auth/<int:id>/', GetToken.as_view(), name='get_token'),
    path('createuser/', UserCreateOrListView.as_view(), name='user_create_or_list'),
]
