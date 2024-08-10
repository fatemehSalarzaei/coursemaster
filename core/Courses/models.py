from django.db import models
from django.utils import timezone

from Courses.models import Instructor


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    STATUS_CHOICES = [
        ('Registering', 'Registering'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    DELIVERY_CHOICES = [
        ('Online', 'Online'),
        ('In-person', 'In-person'),
    ]

    title = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    description = models.TextField()
    num_students = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Registering')
    registration_start = models.DateField()
    registration_end = models.DateField()
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='Online')
    location = models.CharField(max_length=255, blank=True, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title
