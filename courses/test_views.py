from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from .models import Course, Enrolment


class CourseViewTestCase(TestCase):

    def setUp(self):

        course = Course.objects.create(
            course_code="XXXXX", 
            course_name="YYYYY", 
            semester="1", 
            year="2022", 
            seat="99", 
            quota="OPEN"
        )
        enrolment = Enrolment.objects.create(
            first_name="harry", last_name="potter")
        course.enrolments.add(enrolment)

    def test_index_view_status_code(self):
        """ index view's status code is ok """

        c = Client()
        response = c.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        """ context is correctly set """

        c = Client()
        response = c.get(reverse('courses:index'))
        self.assertEqual(
            response.context['courses'].count(), 1)

    def test_valid_course_page(self):
        """ valid course page should return status code 200 """

        c = Client()
        f = Course.objects.first()
        response = c.get(reverse('courses:course', args=(f.id,)))
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_page(self):
        """ invalid course page should return status code 404 """

        max_id = Course.objects.all().aggregate(Max("id"))['id__max']

        c = Client()
        response = c.get(reverse('courses:course', args=(max_id+1,)))
        self.assertEqual(response.status_code, 404)

    def test_cannot_enroll_nonavailable_seat_course(self):
        """ cannot enroll full seat course"""

        enrolment = Enrolment.objects.create(
            first_name="hemione", last_name="granger")
        f = Course.objects.first()
        f.seat = 1
        f.save()

        c = Client()
        c.post(reverse('courses:enroll', args=(f.id,)),
               {'enrolment': enrolment.id})
        self.assertEqual(f.enrolments.count(), 1)
        
    def test_cannot_cancel_seat_course(self):
        """ cannot cancel non-enrolment course """

        enrolment = Enrolment.objects.create(
            first_name="hemione", last_name="granger")
        f = Course.objects.first()
        f.seat = 1
        f.save()

        c = Client()
        c.post(reverse('courses:cancel', args=(f.id,)),
               {'enrolment': enrolment.id})
        self.assertEqual(f.seat - f.enrolments.count(), 0)