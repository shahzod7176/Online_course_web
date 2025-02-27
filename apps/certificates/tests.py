from django.test import TestCase
from django.contrib.auth import get_user_model
from certificates.models import Certificate

User = get_user_model()


class CertificateModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.certificate = Certificate.objects.create(user=self.user, course="Python Backend")

    def test_certificate_creation(self):
        self.assertEqual(str(self.certificate), "testuser - Python Backend")
        self.assertFalse(self.certificate.is_verified)
