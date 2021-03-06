# Generated by Django 4.0 on 2022-01-06 19:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_alter_teammember_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='phone_number',
            field=models.CharField(default='0', max_length=17, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='([+][0-9])?[-| ]?[0-9]{3}[-| ]?[0-9]{3}[-| ]?[0-9]{4}$')]),
        ),
    ]
