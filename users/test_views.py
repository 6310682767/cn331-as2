from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse

class CourseViewTestCase(TestCase):
    
    def setUp(self):
        
        self.user = User.objects.create_user(
            email='john@gmail.com',
            password='lennon',
            username='john'
        )
        
    def test_index_view_status_code(self):
        """ index view's status code is ok """

        c = Client()
        c.force_login(self.user)
        response = c.post(reverse('users:index'), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_login_to_index_page(self):
        """ login to index's page """

        c = Client()
        response = c.post(reverse('users:login'), {
            'username': self.user.username,
            'password': self.user.password
        })
        self.assertEqual(response.status_code, 200)
        
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
