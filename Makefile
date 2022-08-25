install:
	pip install -v --upgrade pip && pip install -vr requirements.txt
	
format:
	black *.py
	
lint:
	pylint --disable=R,C palindrome.py
	
test:
	python -m pytest -vv --cov=palindrome test_palindrome.py
	
all: install format lint test