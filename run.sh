#!/bin/sh

IMAGE_NAME = honeycomb

docker build -t $(IMAGE_NAME) .
docker run -p 5000:5000 $(IMAGE_NAME)