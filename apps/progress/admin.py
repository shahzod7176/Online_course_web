from django.contrib import admin
from progress.models import Progress


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'completed_lessons', 'progress_percentage', 'last_updated']
    list_filter = ['user', 'course']
    search_fields = ['user__username', 'course__title']
