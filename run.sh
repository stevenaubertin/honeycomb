#!/bin/sh

IMAGE_NAME=x0r/honeycomb
CONTAINER_NAME=honeycomb

docker build -t $IMAGE_NAME .
docker run -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME