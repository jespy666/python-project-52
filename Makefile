dev:
	poetry run python3 manage.py runserver

makemessages:
	django-admin makemessages --ignore="static" --ignore=".env" -l ru

compile:
	django-admin compilemessages

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

lint:
	poetry run flake8 task_manager