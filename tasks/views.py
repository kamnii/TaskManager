from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import (TaskSerializer)


@api_view(['GET'])
def task_list_api_view(request):
    tasks = Task.objects.all()
    data = TaskSerializer(tasks, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)