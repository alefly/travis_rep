.PHONY: build start stop healthcheck
build: Dockerfile copy/server.py
	docker build -t alefly/server:v1 . &
run:
	docker run --name server alefly/server:v1 &
start:
	docker start server
stop: 
	docker stop server
healthcheck:
	docker --version
	python3 --version

