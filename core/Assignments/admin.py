from django.contrib import admin
from .models import Exam, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'exam', 'question_type')
    inlines = [ChoiceInline]

class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'session', 'exam_date', 'status')
    list_filter = ('status', 'exam_date')
    search_fields = ('title', 'session__title')

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
