# Generated by Django 5.0.7 on 2024-08-10 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Instructors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/')),
                ('description', models.TextField()),
                ('num_students', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('Registering', 'Registering'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Registering', max_length=20)),
                ('registration_start', models.DateField()),
                ('registration_end', models.DateField()),
                ('delivery_method', models.CharField(choices=[('Online', 'Online'), ('In-person', 'In-person')], default='Online', max_length=10)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='Courses.category')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='Instructors.instructor')),
            ],
        ),
    ]