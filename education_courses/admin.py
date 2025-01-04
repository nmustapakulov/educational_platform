from django.contrib import admin
from .models import Category, Course, Section, Lecture
# Register your models here.

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lecture)
