from tkinter import DoubleVar
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import contact
from myapp .serializers import contactSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def api_list(request):
    
 if request.method == 'GET':
        snip = contact.objects.all()
        serializer = contactSerializer(snip, many=True)
        return Response(serializer.data)

 elif request.method == 'POST':
        serializer = contactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
      
@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
  
    try:
        snip = contact.objects.get(pk=pk)
    except contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = contactSerializer(snip)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = contactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)