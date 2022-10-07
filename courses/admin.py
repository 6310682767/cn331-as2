
from django.contrib import admin
from .models import Course, Enrolment

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_code", "course_name", "semester", "year", "quota", "seat")

class EnrolmentAdmin(admin.ModelAdmin):
    filter_horizontal = ['courses',]
    list_display = ("first_name", "last_name")
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrolment, EnrolmentAdmin)