install: 
	virtualenv -p python3 venv 
	venv/bin/pip install -r requirements.txt 
	venv/bin/python manage.py migrate 

install-db: 
	./scripts/postgres.sh 

run:
	venv/bin/python manage.py runserver