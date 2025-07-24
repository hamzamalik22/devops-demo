from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'completed', 'created_at', 'updated_at')
    list_filter = ('status', 'completed')
    search_fields = ('title',)

admin.site.register(Todo, TodoAdmin)
