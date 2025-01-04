"""Определяет схемы URL для education_courses."""

from django.urls import path

from . import views

app_name = 'education_courses'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    #Страница со списком всех курсов.
    path('courses/', views.courses, name='courses'),
]