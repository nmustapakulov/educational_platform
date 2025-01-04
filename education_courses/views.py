from django.shortcuts import render
from .models import Course

def index(request):
    """Домашняя страница приложения education_courses"""
    return render(request, 'education_courses/index.html')

def courses(request):
    """Выводит список курсов."""
    courses = Course.objects.order_by('date_added')
    context = {'courses':courses}
    return render(request, 'education_courses/courses.html', context)

def course(request, course_id):
    course = Course.objects.get(id=course_id)
    sections = course.section_set.order_by('order')
    context = {'course': course, 'sections': sections}
    return render(request, 'education_courses/course.html', context)