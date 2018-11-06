#!/usr/bin/make

USER=javipolo
NAME=http-show-headers
VERSION=0.1
IMAGE=${USER}/${NAME}:${VERSION}
LATEST=${USER}/${NAME}:latest

all: build

run: ## Run image
	sudo docker run ${IMAGE}

shell: ## Run image and get a shell
	sudo docker run -it ${IMAGE} sh

build: ## Build image
	sudo docker build -t ${IMAGE} .
	sudo docker tag ${IMAGE} ${LATEST}

push: ## Push image to docker
	sudo docker push ${IMAGE}
	sudo docker push ${LATEST}

help:   ## Shows this message.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all build publish help
