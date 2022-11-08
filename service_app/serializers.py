from rest_framework import fields, serializers
from .models import Clients, Services,  Booking 


class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Clients
        fields = ("id","name_of_services", "service_place", "client_name", "client_email","client_date_of_birth","client_point_of_service")


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Services
        fields = ("id","type_of_service", "service_price", "service_duration", "name_of_master")

class BookingSerializer(serializers.ModelSerializer):
    client = ClientsSerializer
    service = ServicesSerializer
    class Meta:
        model  = Booking
        fields =("name_of_services", "client_name", "type_of_service", "start_date", "end_date", "it_finished")        

                
