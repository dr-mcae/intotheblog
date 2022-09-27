SHELL = /bin/sh

CURRENT_USER := $(shell id -u):$(shell id -g)
DJANGO_SUPERUSER_PASSWORD:= intotheblog

export CURRENT_USER
export DJANGO_SUPERUSER_PASSWORD

all: build_images run_images setup_env

build_images:
	docker-compose build

run_images:
	mkdir -p docker-data/media
	docker-compose up -d

setup_env:
	sleep 8
	docker exec intotheblog_python_1 python manage.py migrate
	-docker exec -e DJANGO_SUPERUSER_PASSWORD=$$DJANGO_SUPERUSER_PASSWORD intotheblog_python_1 python manage.py createsuperuser --no-input --username admin --email mail@localhost
	docker restart intotheblog_python_1

stop:
	docker-compose down