from django.test import TestCase
from django.contrib.auth import get_user_model
from courses.models import Course
from reviews.models import Review

User = get_user_model()


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.course = Course.objects.create(title="Python Backend", description="Django va DRF bo‘yicha kurs")
        self.review = Review.objects.create(user=self.user, course=self.course, rating=5, comment="Zo‘r kurs!")

    def test_review_str_method(self):
        self.assertEqual(str(self.review), f"{self.user.username} - {self.course.title}: 5/5")

    def test_unique_review_per_user_per_course(self):
        with self.assertRaises(Exception):
            Review.objects.create(user=self.user, course=self.course, rating=4, comment="Yaxshi!")
