# Generated by Django 5.0.2 on 2024-02-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_trustedperson_phone_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='selected_option',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]