import json

from django.shortcuts import render
from django.http import JsonResponse

from vehicles_demo.apps.vehicles.models import Vehicles


def search(request):
    queryset = Vehicles.objects.all()
    is_online_filter = request.GET.get('online')
    customer_filter = request.GET.get('customer_name')
    if is_online_filter is not None:
        queryset = queryset.filter(online=json.loads(is_online_filter))

    if customer_filter is not None:
        queryset = queryset.filter(customer__name__contains=customer_filter)

    return JsonResponse (
        [
            {
                'id': vehicle.id,
                'vin': vehicle.vin,
                'reg_no': vehicle.reg_no,
                'customer' : {
                    'id': vehicle.customer.id,
                    'name': vehicle.customer.name,
                    'address': vehicle.customer.address
                },
                'online': vehicle.online
            } for vehicle in queryset.all() ],
        safe=False
    )