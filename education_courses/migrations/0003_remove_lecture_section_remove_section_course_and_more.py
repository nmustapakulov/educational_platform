# Generated by Django 4.2.17 on 2025-01-03 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education_courses', '0002_course_section_lecture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='section',
        ),
        migrations.RemoveField(
            model_name='section',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
