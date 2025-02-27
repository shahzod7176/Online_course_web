from rest_framework import serializers
from progress.models import Progress


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'user', 'course', 'completed_lessons', 'progress_percentage', 'last_updated']
        read_only_fields = ['user', 'progress_percentage', 'last_updated']
