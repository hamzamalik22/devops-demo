from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

# Minimal view to list and add todos

def todo_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
            return redirect('todo_list')
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})
