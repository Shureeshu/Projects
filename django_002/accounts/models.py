# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)  # 추가
    pass
    # ... fields ...

# id : PK
# username
# first_name
# last_name
# email
# password
# is_staff
# is_activate
# is_superuser
# last_login
# data_joined
