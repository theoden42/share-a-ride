from django.db import models
from ..user.models import Profile
from datetime import datetime


class Ride(models.Model):
    user_initiator = models.ForeignKey(Profile, on_delete=models.PROTECT)
    src_location = models.CharField(max_length=100)
    dst_location = models.CharField(max_length=100)
    total_fare = models.IntegerField()
    num_passengers = models.IntegerField()
    start_datetime = models.DateTimeField()
