from django import forms

from .models import Course, Section, Lecture

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category', 'title', 'description']

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'order']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['section', 'title', 'description', 'video_url']