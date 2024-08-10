from django.contrib import admin
from .models import Course, Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'start_date', 'end_date', 'status', 'delivery_method', 'instructor', 'category')
    list_filter = ('status', 'delivery_method', 'category')
    search_fields = ('title', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
