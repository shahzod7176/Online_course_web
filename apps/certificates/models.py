import uuid

from django.db.models import UUIDField, CharField, DateField, Model


class Certificate(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)
    issued_by = CharField(max_length=255)
    issue_date = DateField()
    expiration_date = DateField(null=True, blank=True)

    def __str__(self):
        return self.name
