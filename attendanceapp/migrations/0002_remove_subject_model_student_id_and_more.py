# Generated by Django 4.2.17 on 2025-01-14 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject_model',
            name='STUDENT_ID',
        ),
        migrations.AlterField(
            model_name='subject_model',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendanceapp.staff_model'),
        ),
    ]