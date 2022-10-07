from django.db import models
import datetime

class Course(models.Model):
    SEMESTER = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3/Summer'),
    ]
    
    QUOTA = [
        ('OPEN', 'OPEN'),
        ('CLOSED', 'CLOSED'),
    ]

    course_code = models.CharField(max_length=5)
    course_name = models.CharField(max_length=64)
    semester = models.CharField(max_length=1, default=1, choices=SEMESTER) 
    year = models.IntegerField(default=datetime.datetime.now().year)
    seat = models.PositiveIntegerField(default=99)
    quota = models.CharField(max_length=64, default='OPEN', choices=QUOTA)
    
    def __str__(self):
        return f"{self.course_code} | {self.course_name}"
    
    def is_seat_available(self):
        return self.enrolments.count() < self.seat
    
    def is_quota_available(self):
        return self.quota == "OPEN"

class Enrolment(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, blank=True, related_name='enrolments')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"