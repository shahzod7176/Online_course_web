from django.urls import path
from progress.views import ProgressListCreateView, ProgressDetailView

urlpatterns = [
    path('', ProgressListCreateView.as_view(), name='progress-list'),
    path('<int:pk>/', ProgressDetailView.as_view(), name='progress-detail'),
]
