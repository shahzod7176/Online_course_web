from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from notifications.models import Notification
from notifications.serializers import NotificationSerializer


@extend_schema(tags=['notifications'])
class NotificationListCreateView(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(tags=['notifications'])
class NotificationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
