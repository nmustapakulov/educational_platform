"""Определяет схемы URL для education_courses."""

from django.urls import path

from . import views

app_name = 'education_courses'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    #Страница со списком всех курсов.
    path('courses/', views.courses, name='courses'),
    #Страница с подробной информацией о курсе.
    path('courses/<int:course_id>/', views.course, name='course'),
    #Страница для добавления новой темы.
    path('new_course/', views.new_course, name='new_course'),
    # Страница для добавления новый разделов для курса.
    path('new_entry/<int:course_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования разделов курса.
    path('edit_section/<int:section_id>/', views.edit_section, name='edit_section'),
    # Страница для редактирования лекции курса.
    path('edit_lectures/<int:lecture_id>/', views.edit_lecture, name='edit_lecture'),
    # Страница для добавления новых лекции курса.
    path('new_lecture/<int:section_id>/', views.new_lecture, name='new_lecture'), 
]