from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']
