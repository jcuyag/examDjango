from django.contrib import admin

# Register your models here.


from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'description', 'status']
    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)