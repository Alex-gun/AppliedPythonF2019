from django.db import models
import datetime
import time


class Airport(models.Model):
    airport_name = models.CharField(verbose_name="airport name", max_length=100, primary_key=True)

    class Meta:
        db_table = 'airport'


class Aircraft(models.Model):
    aircraft_type = models.CharField(verbose_name="airport name", max_length=100, primary_key=True)

    class Meta:
        db_table = 'aircraft'


class AirFlight(models.Model):
    departure_time = models.DateTimeField("departure time", db_index=True)
    arrival_time = models.DateTimeField("arrival time", db_index=True)
    travel_time = models.PositiveIntegerField("travel time", db_index=True)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    def __init__(self, **kwargs):
        self.travel_time = kwargs["departure_time"]
        super().__init__(self, **kwargs)

    class Meta:
        db_table = 'airflight'
