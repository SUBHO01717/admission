# Generated by Django 4.2.6 on 2023-11-19 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_alter_university_accept_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='accept_student',
            field=models.CharField(blank=True, choices=[('Home', 'Home'), ('Foreign', 'Foreign')], default=None, max_length=30, null=True),
        ),
    ]
