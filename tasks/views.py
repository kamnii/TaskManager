from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import (TaskSerializer)


@api_view(['GET', 'POST'])
def task_list_api_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        data = TaskSerializer(tasks, many=True).data

        return Response(data=data,
                    status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
