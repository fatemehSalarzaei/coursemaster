from django.contrib import admin
from .models import Notification , InstructorNotification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_global', 'user', 'created_at')
    list_filter = ('is_global', 'created_at')
    search_fields = ('message', 'user__username')

class InstructorNotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_global', 'course', 'specific_student', 'created_at')
    list_filter = ('is_global', 'created_at', 'course')
    search_fields = ('message', 'course__title', 'specific_student__username')

admin.site.register(Notification, NotificationAdmin)
admin.site.register(InstructorNotification, InstructorNotificationAdmin)
