from django.contrib import admin

from .models import Clients
admin.site.register(Clients)

from .models import Services
admin.site.register(Services)

from .models import Booking
admin.site.register(Booking)
