install:
	pip install --upgrade pip &&\
		pip install -r Requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black hlib/*.py 
	
#refactor: format lint

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py hlib/*.py 

all: install lint test