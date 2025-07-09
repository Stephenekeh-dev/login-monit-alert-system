from django.contrib import admin
from .models import FailedLoginAttempt

@admin.register(FailedLoginAttempt)
class FailedLoginAttemptAdmin(admin.ModelAdmin):
    list_display = ('email', 'attempt_count', 'timestamp', 'observation')
    search_fields = ('email', 'observation')
    list_filter = ('timestamp', 'observation')