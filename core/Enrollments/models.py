from django.db import models
from django.utils import timezone

from Students.models import Student
from Courses.models import Course

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),  # ثبت‌نام شده
        ('Completed', 'Completed'),  # اتمام یافته
        ('Withdrawn', 'Withdrawn'),  # انصراف داده شده
        ('Dropped', 'Dropped'),  # حذف شده
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')  # دانشجو
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')  # دوره
    enrollment_date = models.DateField(default=timezone.now)  # تاریخ ثبت‌نام
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enrolled')  # وضعیت ثبت‌نام
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # پیشرفت در دوره به درصد
    final_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # نمره نهایی

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.course.title} ({self.status})"
