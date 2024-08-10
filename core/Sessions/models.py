from django.db import models
from django.utils import timezone

from Courses.models import Course
from Enrollments.models import Enrollment

class Session(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'), 
        ('Ongoing', 'Ongoing'),      
        ('Completed', 'Completed'),  
        ('Cancelled', 'Cancelled'),  
    ]
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sessions')  
    duration = models.DurationField()  
    date = models.DateTimeField()  
    handout = models.FileField(upload_to='sessions/handouts/', null=True, blank=True) 
    link = models.URLField(max_length=200, blank=True, null=True) 
    description = models.TextField(blank=True, null=True)  
    title = models.CharField(max_length=255)  
    location = models.CharField(max_length=255, blank=True, null=True) 
    content = models.TextField(blank=True, null=True)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')  
    def __str__(self):
        return f"{self.title} - {self.course.title}"

from django.db import models

class Attendance(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
    ])
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.enrollment.student} - {self.session} - {self.status}"
    
class Feedback(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.enrollment.student} - {self.session} - Rating: {self.rating}"
