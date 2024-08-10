from django.contrib import admin
from .models import Session ,  Attendance , Feedback

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'date', 'status', 'duration', 'location')
    list_filter = ('status', 'course')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'session', 'status', 'date')
    list_filter = ('status', 'date', 'session')
    search_fields = ('enrollment__student__user__username', 'session__title')
    ordering = ('-date',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'session', 'rating', 'comment')
    list_filter = ('rating', 'session')
    search_fields = ('enrollment__student__user__username', 'session__title')
    ordering = ('-session',)

