from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
 
from users.models import User


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
