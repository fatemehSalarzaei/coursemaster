# Generated by Django 5.0.7 on 2024-08-10 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Assignments', '0001_initial'),
        ('Enrollments', '0001_initial'),
        ('Sessions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sessions.session'),
        ),
        migrations.AddField(
            model_name='question',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='Assignments.exam'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='Assignments.question'),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assignments.question'),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='selected_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Assignments.choice'),
        ),
        migrations.AddField(
            model_name='studentexam',
            name='enrollment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enrollments.enrollment'),
        ),
        migrations.AddField(
            model_name='studentexam',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assignments.exam'),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='student_exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='Assignments.studentexam'),
        ),
    ]