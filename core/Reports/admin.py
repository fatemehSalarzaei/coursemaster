from django.contrib import admin
from .models import Report, ExamAnalysis, NotificationAnalysis

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'generated_at')
    search_fields = ('report_type',)

class ExamAnalysisAdmin(admin.ModelAdmin):
    list_display = ('exam', 'average_score', 'highest_score', 'lowest_score', 'generated_at')
    search_fields = ('exam__title',)

class NotificationAnalysisAdmin(admin.ModelAdmin):
    list_display = ('notification', 'total_sent', 'total_delivered', 'total_failed', 'generated_at')
    search_fields = ('notification__message',)

admin.site.register(Report, ReportAdmin)
admin.site.register(ExamAnalysis, ExamAnalysisAdmin)
admin.site.register(NotificationAnalysis, NotificationAnalysisAdmin)
