from rest_framework.authentication import BaseAuthentication
from users.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('username')
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such user')
        return (user, None)
