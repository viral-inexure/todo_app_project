from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    create_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.category_name


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    deadline_time = models.DateTimeField(default=now)
    is_important = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    create_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.title


class TodoCategoryMapping(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.todo)


class NotificationMassages(models.Model):
    massage_title = models.CharField(max_length=200)
    massage_description = models.TextField(max_length=300)

    def __str__(self):
        return self.massage_title


class Notification(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_massage = models.ForeignKey(NotificationMassages, on_delete=models.CASCADE)
    is_send = models.BooleanField(default=False)
    sand_datetime = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.notification_massage)