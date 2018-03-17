.PHONY: dev production install test build run inspect shell stop clean

IMAGE_NAME = pi-home-monitor-image
CONTAINER_NAME = pi-home-monitor-container

dev: 
	FLASK_APP=src/app.py FLASK_DEBUG=1 flask run

production:
	FLASK_APP=src/app.py flask run --host=0.0.0.0 --port=80

install:
	pip3 install -r requirements.txt

test:
	py.test

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -p 80:80 --name $(CONTAINER_NAME) $(IMAGE_NAME)

inspect:
	docker inspect $(CONTAINER_NAME)

shell:
	docker exec -it $(CONTAINER_NAME) /bin/sh

stop:
	docker stop $(CONTAINER_NAME)

clean:
	docker rm -f $$(docker ps -aqf "name=$(CONTAINER_NAME)") || true
	docker rmi -f $$(docker images $(IMAGE_NAME) -q)