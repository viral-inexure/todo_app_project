# Generated by Django 3.2.6 on 2021-08-25 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('My_todo_app', '0013_auto_20210823_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='My_todo_app.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='update_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='update_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='update_time',
            field=models.DateTimeField(),
        ),
    ]
