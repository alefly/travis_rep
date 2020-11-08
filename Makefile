.PHONY: build start stop healthcheck

build: docker-compose.yaml
	docker-compose build
	
start:
	docker-compose up
	
stop: 
	docker-compose down
	
clean: stop
	docker rmi alefly/server:v2 
		
healthcheck:
	docker --version
	python3 --version
	docker-compose --version

