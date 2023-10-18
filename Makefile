dev:
	poetry run python3 manage.py runserver

makemessages:
	django-admin makemessages --ignore="static" -l ru

compile:
	django-admin compilemessages

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

lint:
	poetry run flake8 task_manager

install:
	poetry install