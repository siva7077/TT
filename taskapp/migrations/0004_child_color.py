# Generated by Django 5.0.2 on 2024-03-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_attendance_selected_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]