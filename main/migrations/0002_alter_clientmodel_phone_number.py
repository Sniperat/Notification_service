# Generated by Django 4.2.1 on 2023-05-11 19:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '7XXXXXXXXX'. Up to 15 digits allowed.", regex='^\\7?1?\\d{10}$')]),
        ),
    ]