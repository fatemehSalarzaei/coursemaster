# Generated by Django 5.0.7 on 2024-08-10 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0001_initial'),
        ('Enrollments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField()),
                ('date', models.DateTimeField()),
                ('handout', models.FileField(blank=True, null=True, upload_to='sessions/handouts/')),
                ('link', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled', max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='Courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.PositiveIntegerField(default=0)),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enrollments.enrollment')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sessions.session')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late'), ('excused', 'Excused')], max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enrollments.enrollment')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sessions.session')),
            ],
        ),
    ]
