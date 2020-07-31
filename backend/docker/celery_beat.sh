#!/bin/bash

FILE=celerybeat.pid

if [ -f "$FILE" ]; then
    echo "Deleting old process file"
    rm celerybeat.pid
fi

celery beat -A vehicles_demo -l info
