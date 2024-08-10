from django.db import models
from django.utils import timezone

from Students.models import Student
from Courses.models import Course

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),  
        ('Completed', 'Completed'),  
        ('Withdrawn', 'Withdrawn'), 
        ('Dropped', 'Dropped'),  
    ]

    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),       
        ('Paid', 'Paid'),               
        ('Failed', 'Failed'),           
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments') 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')  
    enrollment_date = models.DateField(default=timezone.now)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enrolled')  
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')  
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  
    final_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.course.title} ({self.status})"
