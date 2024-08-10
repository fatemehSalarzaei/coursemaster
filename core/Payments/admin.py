from django.contrib import admin
from .models import DiscountCode, Payment, Invoice, Enrollment

@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percentage', 'valid_from', 'valid_to', 'is_active')
    search_fields = ('code',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'amount', 'payment_date', 'payment_method', 'transaction_id')
    list_filter = ('payment_method', 'enrollment__course')
    search_fields = ('transaction_id', 'enrollment__student__user__first_name', 'enrollment__student__user__last_name', 'enrollment__course__title')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'amount_due', 'amount_paid', 'issue_date', 'due_date', 'status')
    list_filter = ('status', 'enrollment__course')
    search_fields = ('enrollment__student__user__first_name', 'enrollment__student__user__last_name', 'enrollment__course__title')
    date_hierarchy = 'issue_date'
