from django.shortcuts import render
from .models import Course

def index(request):
    """Домашняя страница приложения education_courses"""
    return render(request, 'education_courses/index.html')

def courses(request):
    #"""Выводит список курсов."""
    courses = Course.objects.order_by('date_added')
    context = {'courses':courses}
    return render(request, 'education_courses/courses.html', context)
