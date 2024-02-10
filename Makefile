# Initialization rule
init:
	pip install -r requirements.txt

# Test rule
test:
	python -m unittest discover -s DataAccess.tests -p 'test*.py'
	python -m unittest discover -s GenericValidators.tests -p 'test*.py'

# Clean rule
clean:
	rm -rf build/ dist/ *.egg-info/


#to run makefile : make init/ make test...