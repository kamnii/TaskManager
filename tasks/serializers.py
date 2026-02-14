from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at']

    def get_status(self, obj):
        if obj.is_completed:
            return "Выполнено"
        return "В процессе"