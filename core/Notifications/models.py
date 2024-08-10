from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from Courses.models import Course

class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_global = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')

    def __str__(self):
        if self.is_global:
            return f"Global Notification: {self.message[:50]}"
        return f"Notification for {self.user.username}: {self.message[:50]}"
    
class InstructorNotification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_global = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    specific_student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='specific_notifications')

    def __str__(self):
        if self.is_global:
            return f"Global Notification for Course {self.course.title if self.course else 'All Courses'}: {self.message[:50]}"
        return f"Notification for {self.specific_student.username} in Course {self.course.title if self.course else 'None'}: {self.message[:50]}"
