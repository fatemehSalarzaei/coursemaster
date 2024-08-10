from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from Students.models import Student
from Courses.models import Course
from Enrollments.models import Enrollment

class DiscountCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Other', 'Other'),
    ]
    
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Payment {self.transaction_id} for {self.enrollment.course.title}"

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ]
    
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='invoices')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    issue_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True, blank=True, related_name='invoice')

    def __str__(self):
        return f"Invoice {self.id} for {self.enrollment.course.title} - {self.enrollment.student.user.get_full_name()}"
