from django.db import models


class Shipment(models.Model):
    vehicle_name = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=100)
    cargo_weight = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    exportation = models.CharField(max_length=100)
    importation = models.CharField(max_length=100)

    def __str__(self):
        return self.tracking_number
