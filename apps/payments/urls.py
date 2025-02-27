from django.urls import path
from payments.views import PaymentListCreateView, PaymentDetailView

urlpatterns = [
    path('payments/', PaymentListCreateView.as_view(), name='payment-list'),
    path('payments/<uuid:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]
