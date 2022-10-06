from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class CourseViewTestCase(TestCase):
    
    def setUp(self):
        user = User.objects.create(username='john')
        user.set_password('lennon')
        user.save()
       
    def test_login_view_status_code(self):
        """ login view's status code is ok """

        c = Client()
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        
    def test_logout_view_status_code(self):
        """ logout view's status code is ok """

        c = Client()
        response = c.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 200)
        
    def test_index_course_status_code(self):
        """ index course's status code is ok """

        c = Client()
        response = c.get(reverse('users:courses'))
        self.assertEqual(response.status_code, 200)
        
    def test_can_login(self):
        """ can login to user's page """
        
        c = Client()
        login = c.login(username='john', password='lennon')
        self.assertTrue(login)
        


