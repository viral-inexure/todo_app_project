# Generated by Django 3.2.6 on 2021-08-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_todo_app', '0004_alter_client_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]
