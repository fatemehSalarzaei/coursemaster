from django.db import models

from Sessions.models import Session
from Enrollments.models import Enrollment

class Exam(models.Model):
    EXAM_STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    exam_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=EXAM_STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return f"{self.title} - {self.session} ({self.get_status_display()})"

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_type = models.CharField(max_length=50, choices=[
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False'),
        ('short_answer', 'Short Answer'),
    ])

    def __str__(self):
        return f"Question {self.id} for {self.exam}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Choice {self.id} for {self.question}"



class StudentExam(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(blank=True, null=True)

    EXAM_STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=50, choices=EXAM_STATUS_CHOICES, default='not_started')

    def __str__(self):
        return f"Exam {self.exam.title} - {self.enrollment.student.user.username}"

class StudentAnswer(models.Model):
    student_exam = models.ForeignKey(StudentExam, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    answer_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Answer for {self.question.id} by {self.student_exam.enrollment.student.user.username}"
