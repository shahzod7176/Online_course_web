from django.test import TestCase
from django.contrib.auth import get_user_model
from courses.models import Course
from progress.models import Progress

User = get_user_model()


class ProgressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.course = Course.objects.create(title="Python Backend", description="Django va DRF bo‘yicha kurs")
        self.progress = Progress.objects.create(user=self.user, course=self.course, completed_lessons=5)

    def test_progress_percentage(self):
        self.assertEqual(self.progress.progress_percentage, 0.0)  # Chunki `lessons.count()` 0 bo‘lsa, progress 0%

    def test_str_method(self):
        self.assertEqual(str(self.progress), f"{self.user.username} - {self.course.title}: 0.0%")
