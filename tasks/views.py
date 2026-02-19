from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list_api_view(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user)
        data = TaskSerializer(tasks, many=True).data

        return Response(data=data,
                    status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail_api_view(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
    except Task.DoesNotExist:
        return Response(
            {'error': 'задача не найдена'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        data = TaskSerializer(task).data
        return Response(data=data,
                        status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)