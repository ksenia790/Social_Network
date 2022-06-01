from django.contrib.auth import get_user_model
from rest_framework import serializers


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.Field(source='my_token')

    class Meta:
        model = get_user_model()
        fields = ('token',)


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
