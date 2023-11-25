# Generated by Django 4.1 on 2023-11-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forntend', '0007_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
