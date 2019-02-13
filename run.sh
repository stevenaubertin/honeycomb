#!/bin/sh

IMAGE_NAME = x0r/honeycomb

docker build -t $(IMAGE_NAME) .
docker run -p 5000:5000 $(IMAGE_NAME)