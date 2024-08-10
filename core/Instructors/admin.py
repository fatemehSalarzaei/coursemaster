from django.contrib import admin
from .models import Instructor, Specialization, InstructorSpecialization, ProfessionalBackground

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'biography', 'date_become_instructor', 'photo')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    list_filter = ('date_become_instructor',)
    readonly_fields = ('date_become_instructor',)

@admin.register(InstructorSpecialization)
class InstructorSpecializationAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'specialization', 'proficiency', 'level')
    search_fields = ('instructor__user__email', 'specialization__name')
    list_filter = ('level', 'proficiency')


@admin.register(ProfessionalBackground)
class ProfessionalBackgroundAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'job_title', 'company_name', 'start_date', 'end_date')
    search_fields = ('instructor__user__email', 'job_title', 'company_name')
    list_filter = ('start_date', 'end_date')
