from rest_framework import serializers
from django.utils import timezone
from .models import Task, Tag
from users.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'user']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'name': {
                'required': True,
                'max_length': 50,
                'error_messages': {
                    'required': 'Пожалуйста введите название тега',
                    'max_length': 'Название превышает допустимое количество символов'
                }
            },
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user

        return super().create(validated_data)


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        read_only=True,
        format='%d.%m.%Y %H:%M',
        default_timezone=timezone.get_current_timezone()
    )

    tags = TagSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'user', 'tags']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'title': {
                'required': True,
                'min_length': 5,
                'max_length': 255,
                'error_messages':{
                    'required': 'Пожалуйста, введите название задачи!',
                    'min_length': 'Название должно быть длиннее 5 символов!',
                    'max_length': 'Название превышает допустимое количество символов!'
                }
            },
            'description': {
                'required': False,
                'allow_blank': True,
                'max_length': 5000,
                'error_messages':{
                    'max_length': 'Описание превышает допустимое количество символов!'
                }
            },
            'is_completed': {
                'required': False,
                'default': False,
                'help_text': 'Отметьте, если задача выполнена'
            }
        }

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user

        return super().create(validated_data)
