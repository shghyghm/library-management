from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(null=True, auto_now_add=True, name="created_at")
    updated_at = models.DateTimeField(null=True, auto_now=True, name="updated_at")

    class Meta:
        abstract = True

class User(AbstractUser, TimestampMixin):
    fullname = models.CharField(max_length=80, null=True)
    bio = models.CharField(max_length=80, null=True)
    groups = None
    user_permissions = None
    objects = UserManager()

    def __str__(self):
        return str(self.fullname)


