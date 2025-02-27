import uuid
from django.db import models
from django.db.models import ForeignKey, TextField, BooleanField, DateTimeField, Model, UUIDField


class Notification(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = ForeignKey('users.User', on_delete=models.CASCADE)
    message = TextField()
    is_read = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
