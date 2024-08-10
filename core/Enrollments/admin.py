from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'status', 'progress', 'final_grade')
    list_filter = ('status', 'course')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'course__title')
    date_hierarchy = 'enrollment_date'
