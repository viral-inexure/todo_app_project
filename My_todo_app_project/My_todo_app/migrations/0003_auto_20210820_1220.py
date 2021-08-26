# Generated by Django 3.2.6 on 2021-08-20 12:20

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('My_todo_app', '0002_rename_user_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='client',
            name='mobile_number',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 20, 12, 20, 38, 629273, tzinfo=utc)),
        ),
    ]