from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.urls import reverse
from .models import Course, Enrolment

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {
        'courses': courses
    })

def courseInfo(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'courses/course.html', {
        'course': course,
        'enrolments': course.enrolments.all(),
        'nonenrolments': Enrolment.objects.exclude(courses=course).all(),
    })

def enroll(request, course_id):
    if request.method == "POST":
        course = Course.objects.get(pk=course_id)
        enrolment = Enrolment.objects.get(pk=request.POST['enrolment'])
        course.enrolments.add(enrolment)
        return HttpResponseRedirect(reverse('course', args=(course_id,)))
    
def enrollCancel(request, course_id):
     if request.method == "POST":
        course = Course.objects.get(pk=course_id)
        enrolment = Enrolment.objects.get(pk=request.POST['enrolment'])
        course.enrolments.remove(enrolment)
        return HttpResponseRedirect(reverse('course', args=(course_id,)))
    