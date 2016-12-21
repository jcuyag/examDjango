from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.
from .forms import TaskForm
from .models import Task
class TaskFormView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base.html'
    success_url = '.'