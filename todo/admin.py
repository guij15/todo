from django.contrib import admin
from .models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','created_at','updated_at')
    search_fields = ('task',)
    list_filter = ('is_completed',)
    
admin.site.register(Task,TaskAdmin)

# Register your models here.
