#!/bin/bash

celery worker -A vehicles_demo -E -l info
