# Generated by Django 4.0 on 2022-01-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_alter_teammember_member_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='phone_number',
            field=models.CharField(default='0', max_length=10),
        ),
    ]