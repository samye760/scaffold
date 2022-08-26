install:
	pip install -v --upgrade pip && pip install -vr requirements.txt
	
format:
	black *.py
	
lint:
	pylint --disable=R,C *.py
	
test:
	python -m pytest -vv --cov=* *.py
	
all: install format lint test