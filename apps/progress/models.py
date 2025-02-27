from django.contrib.auth import get_user_model
from django.db.models import Model, ForeignKey, CASCADE, IntegerField, FloatField, DateTimeField

from courses.models import Course

User = get_user_model()

class Progress(Model):
    user = ForeignKey(User, CASCADE, related_name="progress")
    course = ForeignKey(Course, CASCADE, related_name="progress")
    completed_lessons = IntegerField(default=0)
    progress_percentage = FloatField(default=0.0)
    last_updated = DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        total_lessons = self.course.lessons.count()
        if total_lessons > 0:
            self.progress_percentage = (self.completed_lessons / total_lessons) * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}: {self.progress_percentage}%"
