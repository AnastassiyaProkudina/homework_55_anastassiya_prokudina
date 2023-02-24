from django.contrib import admin
from to_do_list.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'status', 'date_to_do', 'description', 'created_at', 'updated_at', 'is_deleted',
        'deleted_at')
    list_filter = ('title', 'status', 'date_to_do')
    fields = ('title', 'status', 'date_to_do', 'description')

admin.site.register(Task, TaskAdmin)
