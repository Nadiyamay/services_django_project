from random import choice
from django.db import models
from datetime import datetime
import uuid
from django.urls import reverse 


class Clients(models.Model):

    name_of_services = models.CharField(max_length=20, help_text="Enter the name of service", blank=False,)
    service_place = models.CharField(max_length=20, help_text="Select service place", blank=False) 
    client_name=models.CharField(max_length=35,help_text="Enter client name")
    client_email=models.EmailField(help_text="Enter client email", blank=False)
    client_date_of_birth=models.DateField(help_text="Enter client's birth day")
    client_point_of_service=models.IntegerField(help_text="Enter client's point")
    comment=models.TextField(max_length=250)
    ...

    def __str__(self):
      return self.client_name

      # Metadata
    class Meta:
        ordering = ["-client_name"]

    def __str__(self):
        return self.client_name

class Services(models.Model):

    SERVICES=[
        ("Make-up","Makeup"),
        ("Nails","Nail service"),
        ("Hair","Hair service"),
        ("Cosmetology","Cosmetology"),
        ("Massage","Massage")
    ]
    type_of_service=models.CharField(max_length=30, choices=SERVICES, help_text="Select type of service", blank=False)
    service_price=models.IntegerField(help_text="Enter yuor price")
    service_duration=models.IntegerField(help_text="Enter service duration", blank=False)
    name_of_master=models.TextField(max_length=30, help_text="Enter the name of master")
    ...

    def __str__(self):
        return self.type_of_service

class Booking(models.Model):
    client         = models.ForeignKey(Clients, on_delete=models.CASCADE)
    service        = models.ForeignKey(Services, on_delete=models.CASCADE)
    num_of_guest  = models.IntegerField(default=1)
    start_date  = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    it_finished   = models.BooleanField(default=False)
    

