
from .serializers import TodolistSerializers
from rest_framework.views import APIView
from .models import Todolist
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED
# Create your views here.
class TodolistALLView(APIView):
    def get (self,request,*args,**kwargs):
        all_lists=Todolist.objects.all()
        serializers=TodolistSerializers(all_lists,many=True)
        return Response(serializers.data)

class DetailTodolistsView(APIView):
    def get (self,request,*args,**kwargs):
        todolist_id=kwargs['todolist_id']
        todolist=get_object_or_404(Todolist,id=todolist_id)
        serializer=TodolistSerializers(todolist)
        return Response(serializer.data)

class CreateTodolistViews(APIView):
    def post(self,request,*args,**kwargs):
        serializer = TodolistSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors)

class UpdateTodolistView(APIView):
    def put(self,request,*args,**kwargs):
        todolist= get_object_or_404(Todolist,id=kwargs['todolist_id'])
        serializers=TodolistSerializers(todolist,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class DeleteToDoListView(APIView):
    def __delete__(self,request,*args,**kwargs):
        todolist=get_object_or_404(Todolist,id=kwargs['todolist_id'])
        serializers = TodolistSerializers(todolist, data=request.data)
        todolist.delete()
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response({'msg':'deleted'})