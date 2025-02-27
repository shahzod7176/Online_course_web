from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models import EmailField, TextField, ImageField, BooleanField, ManyToManyField


class User(AbstractUser):
    groups = ManyToManyField(Group, related_name="custom_user_groups")
    user_permissions = ManyToManyField(Permission, related_name="custom_user_permissions")
    email = EmailField(unique=True)
    bio = TextField(blank=True, null=True)
    avatar = ImageField(upload_to='avatars/', blank=True, null=True)
    is_instructor = BooleanField(default=False)

    def __str__(self):
        return self.username
