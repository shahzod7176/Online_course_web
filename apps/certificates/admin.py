from django.contrib import admin
from certificates.models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issued_by', 'issue_date', 'expiration_date')
    search_fields = ('name', 'issued_by')
