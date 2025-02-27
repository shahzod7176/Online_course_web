import uuid
from django.db import models
from django.db.models import UUIDField, ForeignKey, DecimalField, CharField, DateTimeField


class Payment(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = ForeignKey('users.User', on_delete=models.CASCADE)
    amount = DecimalField(max_digits=10, decimal_places=2)
    status = CharField(max_length=20,
                       choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - {self.status}"
