from django.db import models

from Assignments.models import Exam
from  Notifications.models import InstructorNotification

class Report(models.Model):
    generated_at = models.DateTimeField(auto_now_add=True)
    report_type = models.CharField(max_length=255)
    data = models.JSONField()  # برای ذخیره داده‌های گزارش به صورت JSON

    def __str__(self):
        return f"{self.report_type} Report - {self.generated_at}"

class ExamAnalysis(models.Model):
    exam = models.ForeignKey( Exam, on_delete=models.CASCADE)
    average_score = models.FloatField()
    highest_score = models.FloatField()
    lowest_score = models.FloatField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.exam.title} - {self.generated_at}"

class NotificationAnalysis(models.Model):
    notification = models.ForeignKey(InstructorNotification, on_delete=models.CASCADE)
    total_sent = models.IntegerField()
    total_delivered = models.IntegerField()
    total_failed = models.IntegerField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for Notification {self.notification.id} - {self.generated_at}"
