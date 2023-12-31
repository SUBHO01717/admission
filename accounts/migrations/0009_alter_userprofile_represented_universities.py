# Generated by Django 4.2.6 on 2023-11-18 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_university_country'),
        ('accounts', '0008_alter_userprofile_represented_universities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='represented_universities',
            field=models.ManyToManyField(blank=True, related_name='partners', to='backend.university'),
        ),
    ]
