from django.urls import path
from certificates.views import CertificateListCreateView, CertificateDetailView

urlpatterns = [
    path('certificates/', CertificateListCreateView.as_view(), name='certificate-list'),
    path('certificates/<uuid:pk>/', CertificateDetailView.as_view(), name='certificate-detail'),
]
