from django.contrib import admin
from courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'price', 'created_at')
    search_fields = ('title', 'instructor__username')
    list_filter = ('created_at',)
