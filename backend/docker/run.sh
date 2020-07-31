#!/bin/bash

set -e


: ${HOST:=${HOST:='0.0.0.0'}}
: ${PORT:=${PORT:='5000'}}
: ${DJANGO_SETTINGS_MODULE:=${DJANGO_SETTINGS_MODULE:='vehicles_demo.settings.dev'}}

if [[ $ENV == 'development' ]]; then
    uvicorn vehicles_demo.asgi:application --reload --port $PORT --host $HOST
else
    uvicorn vehicles_demo.asgi:application --port $PORT --host $HOST
fi

