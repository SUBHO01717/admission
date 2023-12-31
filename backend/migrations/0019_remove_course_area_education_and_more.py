# Generated by Django 4.1 on 2023-11-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_delete_studenttype'),
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
            field=models.ManyToManyField(blank=True, null=True, to='backend.educationarea'),
        ),
        migrations.AddField(
            model_name='course',
            name='degree_level',
            field=models.ManyToManyField(blank=True, null=True, to='backend.degreelevel'),
        ),
    ]
