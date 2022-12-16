install:
	pip install --upgrade pip &&\
		pip install -r Requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py hlib/*.py

refactor: format lint

test: 
	python -m pytest -vv --cov=mylib --cov=main test.py

build:
	#build container
	docker build -t deploy-fastapi_klap .
run:
	#run docker
	#docker run -p 127.0.0.1:8080:8080 843922add58e

deploy:
	#deploy goes here
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 318295413266.dkr.ecr.us-east-1.amazonaws.com
	docker build -t klap .
	docker tag klap:latest 318295413266.dkr.ecr.us-east-1.amazonaws.com/klap:latest
	docker push 318295413266.dkr.ecr.us-east-1.amazonaws.com/klap:latest
		
all: install lint test format deploy

