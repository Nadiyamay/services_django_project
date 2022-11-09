from django.shortcuts import render

from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Clients, Services, Booking 
from .serializers import ClientsSerializer ,ServicesSerializer, BookingSerializer 


@api_view(['GET', 'POST'])
def clients_list(request):

    if request.method == 'GET':
        clients = Clients.objects.all()
        serializer = ClientsSerializer(clients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def clients_detail(request, pk):

    try:
        client = Clients.objects.get(pk=pk)
    except Clients.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientsSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientsSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def services_list(request):

    if request.method == 'GET':
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def services_detail(request, pk):

    try:
        service = Services.objects.get(pk=pk)
    except Services.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServicesSerializer(service)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServicesSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
