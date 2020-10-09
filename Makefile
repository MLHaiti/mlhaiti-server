install: install-python  install-db install-dep

install-python:
	sudo apt-get install python3.8
	pip3 install virtualenv

install-dep:
	virtualenv -p python3 venv 
	venv/bin/pip install -r requirements/local.txt 
	venv/bin/python manage.py migrate 

install-db: 
	./scripts/postgres.sh 

run:
	venv/bin/python manage.py runserver

clean:
	@find . -type d -name __pycache__ -exec rm -r {} \+

style:
	@black --line-length 119 mlhaiti
	@isort --recursive mlhaiti

quality:
	@black --check --line-length 119 mlhaiti
	@isort --check-only --recursive mlhaiti
	@flake8 mlhaiti