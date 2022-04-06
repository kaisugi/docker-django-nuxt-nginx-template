import os
from django.contrib.auth import get_user_model


def create_superuser(sender, **kwargs):
    User = get_user_model()
    username = os.environ.get('SUPERUSER_NAME')
    password = os.environ.get('SUPERUSER_PASSWORD')
    if username and password:
        if User.objects.filter(is_superuser=True, username=username).exists():
            print('Skip creation since there is already a superuser with the same name')
        else:
            User.objects.create_superuser(
                username=username, password=password,
                is_superuser=True, is_staff=True, is_active=True
            )
