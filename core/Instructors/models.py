from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Specialization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor')
    biography = models.TextField()
    date_become_instructor = models.DateField(default=timezone.now)
    photo = models.ImageField(upload_to='instructors/', null=True, blank=True)
    specializations = models.ManyToManyField(Specialization, through='InstructorSpecialization')

    def __str__(self):
        return f"{self.user.get_full_name()} - Instructor"

class InstructorSpecialization(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    proficiency = models.PositiveIntegerField(default=0)  # For example, a scale from 1 to 100
    level_choices = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ]
    level = models.CharField(max_length=50, choices=level_choices)
    

    class Meta:
        unique_together = ('instructor', 'specialization')  # Ensures that an instructor can't have duplicate entries for the same specialization

    def __str__(self):
        return f"{self.instructor.user.get_full_name()} - {self.specialization.name} - Proficiency: {self.proficiency}, Level: {self.level}"

class EducationalBackground(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='educational_backgrounds')
    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    graduation_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.instructor.user.get_full_name()} - {self.degree} at {self.institution_name}"

class ProfessionalBackground(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='professional_backgrounds')
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.instructor.user.get_full_name()} - {self.job_title} at {self.company_name}"
