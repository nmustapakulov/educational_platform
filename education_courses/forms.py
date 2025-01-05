from django import forms

from .models import Course, Section

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category', 'title', 'description']

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'order']