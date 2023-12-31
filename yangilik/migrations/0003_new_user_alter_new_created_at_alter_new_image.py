# Generated by Django 4.2.5 on 2023-09-10 16:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yangilik', '0002_alter_new_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 10, 21, 53, 7, 145710)),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
