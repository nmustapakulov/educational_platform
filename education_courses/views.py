from django.shortcuts import render

def index(request):
    """Домашняя страница приложения education_courses"""
    return render(request, 'education_courses/index.html')
