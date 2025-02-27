from django.urls import path
from reviews.views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path('<int:course_id>/', ReviewListCreateView.as_view(), name='review-list'),
    path('detail/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
