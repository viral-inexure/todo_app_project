from django.contrib import admin
from .models import Profile, Category, Todo, TodoCategoryMapping, Notification, NotificationMassages


admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(TodoCategoryMapping)
admin.site.register(Notification)
admin.site.register(NotificationMassages)

