from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Tasks
from .serializers import TasksSerializer


class GetTaskInfoView(APIView):
    def get(self, request):
        queryset = Tasks.objects.all()
        serializer_for_queryset = TasksSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response({"status": "Task created", "id": task.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
