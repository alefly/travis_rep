.PHONY: tests
tests: 
	docker run --rm -d --name redis -p 6379:6379 redis 
	docker run --rm -d --name mongo -p 27017:27017 mongo 
	python3 ./scripts/controller.py & 
	

