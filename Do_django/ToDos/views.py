from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import ToDos
from .serializers import ToDosSerializer

# Create your views here.
class AllToDos(APIView):
  def get(self, request,format=None):
    Todos = ToDos.objects.all()
    serializer = ToDosSerializer(Todos, many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None):
    serializer = ToDosSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailedToDos(APIView):
   def get_object(self,pk):
    try:
      return ToDos.objects.get(id=pk)
    except ToDos.DoesNotExist:
      raise Http404 
    
   def get(self, request, pk, format=None):
     ToDo = self.get_object(pk)
     serializer = ToDosSerializer(ToDo)
     return Response(serializer.data)      

   def put(self, request, pk, format=None):
      ToDo = self.get_object(pk)
      serializer = ToDosSerializer(ToDo, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
   def delete(self, request, pk, format=None):
     ToDo = self.get_object(pk)
     ToDo.delete() 
     return Response(status=status.HTTP_204_NO_CONTENT)
    
class CompletedToDos(APIView):
  def get(self, request, format=None):
    ToDo = ToDos.objects.filter(state = True)
    serializer = ToDosSerializer(ToDo, many=True)
    return Response(serializer.data)

class ActiveToDos(APIView):
  def get(self, request, format=None):
    ToDo = ToDos.objects.filter(state = False)
    serializer = ToDosSerializer(ToDo, many=True)
    return Response(serializer.data)

    
      