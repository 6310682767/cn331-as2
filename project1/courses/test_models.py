from django.test import TestCase
from .models import Course, Enrolment


class TestModels(TestCase):

    def test_create_course(self):

        course = Course.objects.create(
            course_code="XXXXX", 
            course_name="YYYYY", 
            semester="1", 
            year="2022", 
            seat="99", 
            quota="OPEN"
        )
        course.save()
        
        self.assertEqual(str(course), "XXXXX | YYYYY")
        
    def test_create_enrolment(self):

        enrolment = Enrolment.objects.create(
            first_name = "harry",
            last_name = "potter"
        )
        enrolment.save()
        
        self.assertEqual(str(enrolment), "harry potter")

   

   