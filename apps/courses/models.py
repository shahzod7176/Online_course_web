import uuid
from django.db import models
from django.db.models import CharField, TextField, ForeignKey, DecimalField, DateTimeField


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=255)
    description = TextField()
    instructor = ForeignKey('users.User', on_delete=models.CASCADE)
    price = DecimalField(max_digits=10, decimal_places=2)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
