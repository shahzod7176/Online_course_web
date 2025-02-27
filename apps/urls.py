from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('payments/', include('payments.urls')),
    path('reviews/', include('reviews.urls')),
    path('certificates/', include('certificates.urls')),
    path('progress/', include('progress.urls')),
    path('notifications/', include('notifications.urls')),
]
