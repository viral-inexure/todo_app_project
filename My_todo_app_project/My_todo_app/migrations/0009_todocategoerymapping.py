# Generated by Django 3.2.6 on 2021-08-23 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('My_todo_app', '0008_auto_20210823_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoCategoeryMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='My_todo_app.categoery')),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='My_todo_app.todo')),
            ],
        ),
    ]
