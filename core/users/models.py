from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=80, unique=True)

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def get_my_token(self):
        return Token.objects.get(user=user)
    
    my_token = property(get_my_token)

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
