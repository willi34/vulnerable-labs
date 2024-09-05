#!/bin/bash

docker build -t token .
docker container run -p 127.0.0.1:5000:5000 -p 127.0.0.1:2222:22 --rm token
