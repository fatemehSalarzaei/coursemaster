from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'picture', 'emergency_name', 'emergency_phone')
    search_fields = ('user__username', 'address', 'emergency_name')
    list_filter = ('address',)
    # readonly_fields = ('user',) 

admin.site.register(Student, StudentAdmin)
