from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import TasksSerializer
from .models import Task


class taskEntry(APIView):
    """
	GET = return all tasks.
	POST = create new task.
	"""

    def get(self, request, format=None):
        
        tasks = get_list_or_404(Task)
        serialized_data = TasksSerializer(tasks, many=True).data
        return Response({'Result':'Sucess', 'Data':serialized_data})    


    def post(self, request, format=None):

        # return Response({'Result': 'Sucess'})  
		serializer = TasksSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response({'Result':'Sucess', 'Data':serializer.data})

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class taskDetail(APIView):
    """
	GET = return a task
	PUT = update a task
    DELETE = delete a task
	"""

    def get(self, request, pk, format=None):
        
        task = get_object_or_404(Task, task_id=pk)
        serialized_data = TasksSerializer(task).data
        return Response({'Result':'Sucess', 'Data':serialized_data})

    def put(self, request, pk, format=None):
        
        task = get_object_or_404(Task, task_id=pk)
        serializer = TasksSerializer(task, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'Result':'Sucess', 'Data':serializer.data})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        
        task = get_object_or_404(Task, task_id=pk)
        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)