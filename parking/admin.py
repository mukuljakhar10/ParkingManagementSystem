from django.contrib import admin
from .models import ParkingHistory, ParkingSpace, User

admin.site.register(ParkingSpace),
admin.site.register(ParkingHistory),
admin.site.register(User),
