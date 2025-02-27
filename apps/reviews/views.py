from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from reviews.models import Review
from reviews.serializers import ReviewSerializer


@extend_schema(tags=['reviews'])
class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs['course_id'])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['reviews'])
class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
