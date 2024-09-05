#!/bin/bash

python3 -m gunicorn --bind 0.0.0.0:5000 --timeout 120 app.main:app
