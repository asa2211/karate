# Generated by Django 4.2.5 on 2023-09-11 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_customuser_role_customuser_roles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='roles',
            new_name='role',
        ),
    ]
