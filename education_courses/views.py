from django.shortcuts import render, redirect
from .models import Course, Section, Lecture
from .forms import CourseForm, SectionForm, LectureForm
from django.contrib.auth.decorators import login_required

def index(request):
    """Домашняя страница приложения education_courses"""
    return render(request, 'education_courses/index.html')

@login_required
def courses(request):
    """Выводит список курсов."""
    courses = Course.objects.order_by('date_added')
    context = {'courses':courses}
    return render(request, 'education_courses/courses.html', context)

@login_required
def course(request, course_id):
    course = Course.objects.get(id=course_id)
    sections = course.section_set.order_by('order')
    context = {'course': course, 'sections': sections}
    return render(request, 'education_courses/course.html', context)

@login_required
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

@login_required
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

@login_required
def edit_section(request, section_id):
    """Редактирует сущестующую раздел"""
    section = Section.objects.get(id=section_id)
    course = section.course

    # Данные не отправлялись; создается пустая форма.
    if request.method != 'POST':
        form = SectionForm(instance=section)
    else:
        # Отправлены данные POST; обработать данные.
        form = SectionForm(instance=section, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('education_courses:course', course_id=course.id)
        
    # Вывести пустую или недействительную форму.
    context = {'section': section, 'course': course, 'form':form}
    return render(request, 'education_courses/edit_section.html', context)

@login_required
def edit_lecture(request, lecture_id):
    lecture = Lecture.objects.get(id=lecture_id)
    section = lecture.section
    course = section.course

    # Данные не отправлялись; создается пустая форма.
    if request.method != 'POST':
        form = LectureForm(instance=lecture)
    else:
        # Отправлены данные POST; обработать данные.
        form = LectureForm(instance=lecture, data=request.POST)
        if form.is_valid():
            new_lecture = form.save(commit=False)
            new_lecture.order = section.order
            new_lecture.save()
            return redirect('education_courses:course', course_id=course.id)
        
    # Вывести пустую или недействительную форму.
    context = {'lecture': lecture, 'section': section, 'form':form}
    return render(request, 'education_courses/edit_lecture.html', context)

@login_required
def new_lecture(request, section_id):
    """Добавляет новую лекцию к разделу курса"""
    section = Section.objects.get(id=section_id)
    course = section.course
    # Данные не отправлялись; создается пустая форма.
    if request.method != 'POST':
        form = LectureForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = LectureForm(data=request.POST)
        if form.is_valid():
            new_lecture = form.save(commit=False)
            new_lecture.section = section
            new_lecture.save()
            return redirect('education_courses:course', course_id=course.id)
        
    # Вывести пустую или недействительную форму.
    context = {'section': section, 'course': course, 'form':form}
    return render(request, 'education_courses/new_lecture.html', context)

