# Generated by Django 4.0 on 2022-01-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_remove_teammember_role_teammember_member_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='role',
            field=models.IntegerField(default=0, verbose_name=[(0, 'Regular'), (1, 'Admin')]),
        ),
    ]
