from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    address = models.TextField(blank=True, null=True) 
    picture = models.ImageField(upload_to='students/', null=True, blank=True) 
    emergency_name = models.CharField(max_length=255, blank=True, null=True) 
    emergency_phone = models.CharField(max_length=20, blank=True, null=True)  

    def __str__(self):
        return f"{self.user.get_full_name()} - Student"
