from django.shortcuts import render
from .models import Shipment
from django.http import HttpResponse


def shipment_list(request, shipment_id):
    shipments = Shipment.objects.all()
    return render(request, 'shipments/shipment_list.html', {'shipments': shipments})


def home(request):
    return render(request, 'shipments/home.html')

# def shipment_create(request):
#     if request.method == 'POST':
#         form = ShipmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     else:
#         form = ShipmentForm()
#         return render(request, 'shipment/shipment_create.html', {'form': form})
