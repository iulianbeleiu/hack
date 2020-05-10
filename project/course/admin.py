from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    list_per_page = 10
