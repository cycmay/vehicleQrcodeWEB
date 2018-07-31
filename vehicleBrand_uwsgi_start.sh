#!/bin/bash
source ./venv/bin/activate
echo `pip list`
uwsgi --socket :8081 --module vehicleBrand.wsgi