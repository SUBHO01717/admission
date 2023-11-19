# Generated by Django 4.2.6 on 2023-11-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_alter_university_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='Country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='Image',
            new_name='image',
        ),
        migrations.AddField(
            model_name='university',
            name='accept_student',
            field=models.CharField(choices=[('HOME', 'HOME'), ('INTERNATIONAL', 'INTERNATIONAL')], default=None, max_length=30),
        ),
    ]
