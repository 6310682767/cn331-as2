from django.test import TestCase
from .models import Course, Enrolment


class CourseTestCase(TestCase):
    
    def setUp(self):

        Course.objects.create(
            course_code="XXXXX", 
            course_name="YYYYY", 
            semester="1", 
            year="2022", 
            seat="99", 
            quota="OPEN"
        )

    def test_seat_available(self):
        """ is_seat_available should be True """

        course = Course.objects.first()

        self.assertTrue(course.is_seat_available())

    def test_seat_not_available(self):
        """ is_seat_available should be False """
        
        course = Course.objects.first()
        
        enrolment = Enrolment.objects.create(
            first_name="harry", last_name="potter")

        course.seat = 1
        course.enrolments.add(enrolment)

        self.assertFalse(course.is_seat_available())
        
    def test_quota_available(self):
        """ is_quota_available should be True """

        course = Course.objects.first()
        
        self.assertTrue(course.is_quota_available())
        
    def test_quota_not_available(self):
        """ is_quota_not_available should be False """

        course = Course.objects.first()
        
        enrolment = Enrolment.objects.create(
            first_name="harry", last_name="potter")

        course.quota = "CLOSED"
        course.enrolments.add(enrolment)
        
        self.assertFalse(course.is_quota_available())
        
        
