build: Dockerfile
	docker build -t alefly/server:v1 .
start:
	docker run --rm alefly/server:v1
stop: 
	docker stop server
healthcheck:
	docker --version
	python3 --version

