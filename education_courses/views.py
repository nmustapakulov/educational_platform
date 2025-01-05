from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm, SectionForm

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

def new_course(request):
    """Определяет новый курс."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = CourseForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('education_courses:courses')
    
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'education_courses/new_course.html', context)

def new_entry(request, course_id):
    """Добавляет новый раздел для курса"""
    course = Course.objects.get(id=course_id)
    # Данные не отправлялись; создается пустая форма.
    if request.method != 'POST':
        form = SectionForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = SectionForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.course = course
            new_entry.save()
            return redirect('education_courses:course', course_id=course.id)
    
    # Вывести пустую или недействительную форму.
    context = {'course': course, 'form': form}
    return render(request, 'education_courses/new_entry.html', context)

