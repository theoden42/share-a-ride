from django.db import models


class Ride(models.Model):
    user_initiator = models.CharField(max_length=100)
    src_location = models.CharField(max_length=100)
    dst_location = models.CharField(max_length=100)
    total_fare = models.IntegerField()
    num_passengers = models.IntegerField()
    start_datetime = models.DateTimeField()
