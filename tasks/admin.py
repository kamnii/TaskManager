from django.contrib import admin
from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['id', 'title']


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    search_fields = ['name', 'user']
