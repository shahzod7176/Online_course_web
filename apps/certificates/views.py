from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from certificates.models import Certificate
from certificates.serializers import CertificateSerializer


@extend_schema(tags=['certificates'])
class CertificateListCreateView(ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(tags=['certificates'])
class CertificateDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]
