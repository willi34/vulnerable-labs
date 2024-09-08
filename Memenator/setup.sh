#!/bin/bash

docker build -t memenator .
docker container run -p 127.0.0.1:3000:3000 -p 127.0.0.1:2222:22 --rm memenator
