from django.shortcuts import render

from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Clients, Services, Booking 
from .serializers import ClientsSerializer ,ServicesSerializer, BookingSerializer 

from collections import namedtuple


nt = namedtuple("object", ["model", "serializers"])
pattern = {
    "client"  : nt(Clients, ClientsSerializer),
    "service" : nt(Services, ServicesSerializer),
    "booking": nt(Booking, BookingSerializer),
}

@api_view(["GET", "POST"])
def ListView(request, api_name):
    print("hello")
    object =  pattern.get(api_name, None)
    if object == None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.all()
        serializers  = object.serializers(object_list, many=True)
        return Response(serializers.data)

    if request.method == "POST":
        serializers = object.serializers(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response(
                serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
                