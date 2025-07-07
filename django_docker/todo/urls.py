from django.urls import path
from .views import todo_list, toggle_todo, edit_todo, delete_todo, get_stats

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('toggle/<int:todo_id>/', toggle_todo, name='toggle_todo'),
    path('edit/<int:todo_id>/', edit_todo, name='edit_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('stats/', get_stats, name='get_stats'),
] 