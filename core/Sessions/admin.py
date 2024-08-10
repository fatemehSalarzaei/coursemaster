from django.contrib import admin
from .models import Session

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'date', 'status', 'duration', 'location')
    list_filter = ('status', 'course')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
