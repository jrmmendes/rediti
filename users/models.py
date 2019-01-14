from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from common.models import IndexedTimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):

    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, blank=True, max_length=50)
    description = models.TextField(blank=True)
    karma = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True, default='default.avatar.png')
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
