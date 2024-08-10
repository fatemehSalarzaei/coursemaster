from django.contrib import admin
from .models import Exam, Question, Choice ,  StudentExam, StudentAnswer

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

class StudentAnswerInline(admin.TabularInline):
    model = StudentAnswer
    extra = 0

class StudentExamAdmin(admin.ModelAdmin):
    list_display = ('exam', 'enrollment', 'date_taken', 'status', 'grade')
    list_filter = ('status', 'date_taken', 'exam__title')
    search_fields = ('enrollment__student__user__username', 'exam__title')
    inlines = [StudentAnswerInline]

admin.site.register(StudentExam, StudentExamAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
