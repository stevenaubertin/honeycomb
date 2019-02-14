#!/bin/sh
# This file was greatly inspired
# from : https://github.com/nikos/python3-alpine-flask-docker/blob/master/Makefile

.PHONY: clean build run stop inspect

IMAGE_NAME=x0re/honeycomb
CONTAINER_NAME=honeycomb
PORT=5000
VERSION=0.1
DESCRIPTION="Flask boilerplate"
PROJECT_NAME="honeycomb"

build:
	docker build --tag $(IMAGE_NAME) .

release:
	docker build \
		--build-arg PROJECT_NAME=$(PROJECT_NAME) \
		--build-arg DESCRIPTION=$(DESCRIPTION) \
		--build-arg PORT=$(PORT) \
		--build-arg VERSION=$(VERSION) \
		--build-arg VCS_REF=`git rev-parse --short HEAD` \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` -t $(IMAGE_NAME) .

run:
	docker run --rm -p 5000:$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

inspect:
	docker inspect $(CONTAINER_NAME)

shell:
	docker exec -it $(CONTAINER_NAME) /bin/sh

stop:
	docker stop $(CONTAINER_NAME)

clean:
	docker ps -a | grep '$(CONTAINER_NAME)' | awk '{print $$1}' | xargs docker rm \ 
	docker images | grep '$(IMAGE_NAME)' | awk '{print $$3}' | xargs docker rmi