from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.courseInfo, name='course'),
    path('<int:course_id>/enroll', views.enroll, name='enroll'),
    path('<int:course_id>/cancel', views.enrollCancel, name='cancel'),
]