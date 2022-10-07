from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrolment

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {
        'courses': courses
    })

def courseInfo(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course.html', {
        'course': course,
        'enrolments': course.enrolments.all(),
        'nonenrolments': Enrolment.objects.exclude(courses=course).all(),
    })

def enroll(request, course_id):
    if request.method == "POST":
        course = get_object_or_404(Course, pk=course_id)
        enrolment = get_object_or_404(Enrolment, pk=int(request.POST['enrolment']))
        if enrolment not in course.enrolments.all() and course.is_seat_available():
            enrolment = Enrolment.objects.get(pk=int(request.POST["enrolment"]))
            enrolment.courses.add(course)
        return HttpResponseRedirect(reverse('courses:course', args=(course_id,)))
    
def enrollCancel(request, course_id):
     if request.method == "POST":
        course = get_object_or_404(Course, pk=course_id)
        enrolment = get_object_or_404(Enrolment, pk=int(request.POST['enrolment']))
        if enrolment in course.enrolments.all():
            enrolment = Enrolment.objects.get(pk=int(request.POST["enrolment"]))
            enrolment.courses.remove(course)
        return HttpResponseRedirect(reverse('courses:course', args=(course_id,)))
    