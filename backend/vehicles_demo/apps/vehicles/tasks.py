import random

from celery import Celery

from vehicles_demo.apps.vehicles.models import Vehicles


app = Celery()


@app.task
def randomize_status():
    for v in Vehicles.objects.all():
        v.online = bool(random.getrandbits(1))
        v.save()
