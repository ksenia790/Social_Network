from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import generics, views
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.authtoken import views as auth_views
from rest_framework.authtoken.models import Token
from rest_framework import status
from . import serializers
from rest_framework.generics import RetrieveAPIView


class GetToken(RetrieveAPIView):
    serializer_class = serializers.TokenSerializer
    def get(self, request, id):
        token = Token.objects.get(user_id=id)
        return Response({"token": token.key})


class UserCreateOrListView(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        qs = get_user_model().objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        """
        Create new user
        """
        return self.create(request)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            user = serializer.save()
            if user:
                token = Token.objects.get(user=user)
                json = serializer.data
                json['token'] = token.key
                headers = self.get_success_headers(serializer.data)
                return Response(
                    json,
                    status=status.HTTP_201_CREATED,
                    headers=headers
                )

    def get(self, request,  *args, **kwargs):
        """
        Return all users list
        """
        return self.list(request, *args, **kwargs)
