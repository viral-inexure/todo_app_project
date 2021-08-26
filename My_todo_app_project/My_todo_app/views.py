from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login
from .models import Todo, Profile, Category
from .form import RegistrationForm


class CustomLoginView(LoginView):
    template_name = "My_todo_app/login.html"
    fields = '__all__'

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = 'My_todo_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "My_todo_app/home.html"
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = context['todo'].filter(user=self.request.user)
        context['count'] = context['todo'].filter(is_completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['todo'] = context['todo'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context


class TaskDetail(DetailView):
    model = Todo
    template_name = "My_todo_app/task_detail.html"
    context_object_name = 'detail_todo'


class TaskCreate(CreateView):
    category = Category.category_name
    model = Todo
    fields = ['category', 'title', 'description', 'deadline_time', 'is_important', 'is_completed']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Todo
    fields = ['title', 'description', 'deadline_time', 'is_important', 'is_completed']
    success_url = reverse_lazy('home')
    context_object_name = 'todo'


class TaskDelete(DeleteView):
    model = Todo
    context_object_name = "delete_task"

    fields = '__all__'
    success_url = reverse_lazy('home')


class UserProfile(CreateView):
    model = Profile
    # fields = '__all__'


def showformdata(request):
    form_obj = RegistrationForm()
    return render(request, 'My_todo_app/register.html', {'form': form_obj})

