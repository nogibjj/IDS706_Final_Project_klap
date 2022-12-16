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

deploy:
	#deploy goes here
		
all: install lint test format deploy

