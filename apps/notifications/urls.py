from django.urls import path
from notifications.views import NotificationListCreateView, NotificationDetailView

urlpatterns = [
    path('notifications/', NotificationListCreateView.as_view(), name='notification-list'),
    path('notifications/<uuid:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
]
