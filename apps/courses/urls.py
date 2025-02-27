from django.urls import path
from courses.views import CourseListCreateView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<uuid:pk>/', CourseDetailView.as_view(), name='course-detail'),
]
