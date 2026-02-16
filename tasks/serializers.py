from rest_framework import serializers
from django.utils import timezone
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(
        format='%d.%m.%Y %H:%M',
        default_timezone=timezone.get_current_timezone()
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at']

    def get_status(self, obj):
        if obj.is_completed:
            return "Выполнено"
        return "В процессе"
