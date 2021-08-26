from django.urls import path, include
from .views import (TaskList,
                    TaskDetail,
                    TaskCreate,
                    TaskUpdate,
                    TaskDelete,
                    UserProfile,
                    CustomLoginView,
                    RegisterPage,)
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path("", TaskList.as_view(), name="home"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>", TaskUpdate.as_view(), name="task-update"),
    path("delete-task/<int:pk>", TaskDelete.as_view(), name="task-delete"),
    path("user_profile/<int:pk>", UserProfile.as_view(), name="user-detail"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    # path('register/', RegisterPage.as_view(), name='register'),
    path("register/", views.showformdata, name="register"),

]
