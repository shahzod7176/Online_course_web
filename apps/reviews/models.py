from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import ForeignKey, Model, CASCADE, PositiveIntegerField, TextField, DateTimeField

from courses.models import Course

User = get_user_model()


class Review(Model):
    user = ForeignKey(User, CASCADE, related_name="reviews")
    course = ForeignKey(Course, CASCADE, related_name="reviews")
    rating = PositiveIntegerField()
    comment = TextField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'course']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.course.title}: {self.rating}/5"
