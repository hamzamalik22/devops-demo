from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Todo

# Create your views here.

# Main view to list and add todos
def todo_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo = Todo.objects.create(title=title)
            return redirect('todo_list')
    
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo/todo_list.html', {'todos': todos})

# AJAX view to toggle todo completion
@csrf_exempt
@require_http_methods(["POST"])
def toggle_todo(request, todo_id):
    try:
        todo = get_object_or_404(Todo, id=todo_id)
        todo.completed = not todo.completed
        todo.save()
        
        return JsonResponse({
            'success': True,
            'completed': todo.completed,
            'message': f'Task {"completed" if todo.completed else "uncompleted"} successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)

# AJAX view to edit todo
@csrf_exempt
@require_http_methods(["POST"])
def edit_todo(request, todo_id):
    try:
        data = json.loads(request.body)
        new_title = data.get('title', '').strip()
        
        if not new_title:
            return JsonResponse({
                'success': False,
                'error': 'Title cannot be empty'
            }, status=400)
        
        todo = get_object_or_404(Todo, id=todo_id)
        todo.title = new_title
        todo.save()
        
        return JsonResponse({
            'success': True,
            'title': todo.title,
            'message': 'Task updated successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)

# AJAX view to delete todo
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_todo(request, todo_id):
    try:
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Task deleted successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)

# AJAX view to get todo stats
def get_stats(request):
    total = Todo.objects.count()
    completed = Todo.objects.filter(completed=True).count()
    pending = total - completed
    
    return JsonResponse({
        'total': total,
        'completed': completed,
        'pending': pending
    })
