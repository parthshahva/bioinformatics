default: build

.PHONY: install
install:
		pip install -r requirements.txt

.PHONY: test
test:
		python -m unittest discover -s test -p 'test_*.py'