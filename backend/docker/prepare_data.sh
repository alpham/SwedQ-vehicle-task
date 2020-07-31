#!/bin/bash

./manage.py migrate

./manage.py loaddata vehicles_demo/fixtures/customers.json
./manage.py loaddata vehicles_demo/fixtures/vehicles.json