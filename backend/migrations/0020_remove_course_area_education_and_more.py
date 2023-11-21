# Generated by Django 4.1 on 2023-11-21 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_remove_course_area_education_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='area_education',
        ),
        migrations.RemoveField(
            model_name='course',
            name='degree_level',
        ),
        migrations.AddField(
            model_name='course',
            name='area_education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.educationarea'),
        ),
        migrations.AddField(
            model_name='course',
            name='degree_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.degreelevel'),
        ),
    ]
