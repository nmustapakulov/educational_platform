from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Модель для хранения категорий курсов."""
    name = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    """Модель для курсов."""
    title = models.CharField(max_length=70)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Section(models.Model):
    """Модель для секций внутри курса."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    def __str__(self):
        return  self.title

class Lecture(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=255) # Название лекции.
    description = models.TextField() # Описание лекции.
    video_url = models.URLField(blank=True, null=True)  # URL для видео-лекции.

    def __str__(self):
        return self.title
